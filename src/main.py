import os
import re
import shutil
from datetime import datetime


def create_backup(source_file_path) -> None:
    backup_timestamp: str = datetime.now().strftime("%m-%d-%y__%H-%M")
    backup_file_path: str = os.path.join(
        os.getcwd(), "src", "backups", f"Sierra4.{backup_timestamp}.config"
    )
    shutil.copy(src=source_file_path, dst=backup_file_path)


def read_config_file(config_file_path) -> bytes:
    with open(file=config_file_path, mode="rb") as binary_file:
        binary_data: bytes = binary_file.read()
        return binary_data


def convert_binary_to_hex(binary_data: bytes, bytes_per_line: int) -> None:
    if binary_data:
        for i in range(0, len(binary_data), bytes_per_line):
            hex_line: str = " ".join(
                f"{byte:02X}" for byte in binary_data[i : i + bytes_per_line]
            )
            print(hex_line)


def extract_data_between_delimiters(binary_data):
    delimiter = bytes.fromhex("00140004")
    matches = re.finditer(re.escape(delimiter), binary_data)

    data_groups = []
    start = None

    for match in matches:
        if start is not None:
            end = match.start()
            data = binary_data[start:end]

            # Extract the last 3 bytes before the delimiter as the group name and decode as text using 'Windows-1252' (ANSI) encoding
            try:
                group_name_bytes = data[-3:]
                group_name = group_name_bytes.decode("Windows-1252")
            except UnicodeDecodeError:
                group_name_bytes_hex = group_name_bytes.hex()
                group_name = f"Hex: {group_name_bytes_hex}"  # Use hexadecimal representation for decoding errors

            # Replace spaces with dots in the group name
            group_name = group_name.replace(" ", ".")

            data_groups.append((group_name, group_name_bytes.hex(), data))
            start = None
        else:
            start = match.end()

    return data_groups


def main():
    config_file_path = os.path.join(os.getcwd(), "src", "Sierra4.config")

    create_backup(source_file_path=config_file_path)

    binary_data = read_config_file(config_file_path=config_file_path)

    if binary_data:
        data_groups = extract_data_between_delimiters(binary_data)
        for i, (group_name, group_name_hex, data_group) in enumerate(data_groups):
            print(f"Group Name: {group_name} ({group_name_hex})")
            print(f"Data Group {i}:\n{data_group.hex()}")
            break
            # need hex representation with group name


if __name__ == "__main__":
    main()
