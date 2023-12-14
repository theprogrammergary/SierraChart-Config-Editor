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
    delimiter = bytes.fromhex("0014000400")
    matches = re.finditer(re.escape(delimiter), binary_data)

    data_groups = []

    for match in matches:
        start = match.start()
        group_name_hex = binary_data[start - 3 : start + 5].hex()
        group_data = binary_data[start + 5 : start + 85].hex()
        data_groups.append((group_name_hex, group_data))

    return data_groups


def format_hex_string(hex_string):
    return " ".join(hex_string[i : i + 2] for i in range(0, len(hex_string), 2))


def format_group_string_to_list(group_data: str) -> list[str]:
    group_size: int = 6
    skip_size: int = 2
    color_hex_values: list[str] = [
        group_data[i : i + group_size]
        for i in range(0, len(group_data), group_size + skip_size)
    ]

    return color_hex_values


def valid_group_data(group_data: str) -> bool:
    color_hex_values = format_group_string_to_list(group_data)

    if len(color_hex_values) != 20:
        return False

    first_color_hex: str = color_hex_values[0]
    colors_are_equal: bool = all(
        color_hex == first_color_hex for color_hex in color_hex_values
    )

    return colors_are_equal


def get_group_data(file_path: str) -> list[tuple[str, str]]:
    binary_data: bytes = read_config_file(config_file_path=file_path)
    valid_data_groups: List[Tuple[str, str]] = []

    if binary_data:
        raw_data_groups: List[Tuple[str, str]] = extract_data_between_delimiters(
            binary_data
        )

        for i, (group_name, group_data) in enumerate(raw_data_groups):
            valid_group = valid_group_data(group_data)
            if valid_group:
                valid_data_groups.append((group_name, group_data))

    return valid_data_groups


def read_and_modify_binary_file(
    file_path: str, group_data_list: list[tuple[str, str]]
) -> None:
    """
    Changes a Sierra4.config file bytes.
    Finds a header position and then updates the color for
    each of the 20 global graphic configs

    Args:
        file_path (str): The path to the binary file.
        search_sequence (tuple): The search sequence to find in the file.
        changes (list): The list of changes to apply.
    """

    with open(file=file_path, mode="rb") as file:
        binary_data: bytes = file.read()

    if binary_data is None:
        return

    for i, (group_name, group_data) in enumerate(group_data_list):
        search_sequence = group_name
        current_values = format_group_string_to_list

        print(f"search {search_sequence}")
        break

    return
    # Convert the second string in the search_sequence tuple to a list of strings
    group_data_str = search_sequence[1]
    color_hex_values = format_group_string_to_list(group_data_str)

    # Find the position of the search sequence
    position: int = binary_data.find(search_sequence[0])

    if position != -1:
        # Apply changes to the bytes following the search sequence
        for change in changes:
            for color_hex in color_hex_values:
                change_bytes = bytes.fromhex(color_hex + "00")  # Add '00' to the end
                binary_data = (
                    binary_data[: position + len(search_sequence[0])]
                    + change_bytes
                    + binary_data[
                        position + len(search_sequence[0]) + len(change_bytes) :
                    ]
                )
                position += len(change_bytes)

        # Write the modified binary data back to the file
        with open(file=file_path, mode="wb") as file:
            file.write(binary_data)

        print("\n\nChanges applied successfully.")
    else:
        print("\n\nSearch sequence not found in the file.")


def main():
    config_file_path: str = os.path.join(os.getcwd(), "src", "DEFAULT4.config")

    create_backup(source_file_path=config_file_path)

    group_data = get_group_data(config_file_path)

    if group_data is not None:
        read_and_modify_binary_file(config_file_path, group_data)

    # TODO:
    # - start with a refactoring of group_name it is confusing....is it a singular or what
    # - dont need to format the current byte when looping through to change binary...instead can
    #       just get the index from the color_map.json


if __name__ == "__main__":
    main()
