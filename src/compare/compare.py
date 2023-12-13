"""
Compares two sierr4.config files and prints out the differences.
This was primarily used to build out the map of the bytes/hex chars.
I would start with the same config file and make one change and then write down the change.
"""
import difflib

ORIGINAL_CONFIG_PATH: str = "C:\\Users\\Garrett\\Desktop\\Sierra4.config"
EDITED_CONFIG_PATH: str = (
    "C:\\Trading Software\\TPH-Sierra-Chart\\Sierra Chart\\Sierra4.config"
)


def read_config_file(config_file_path) -> bytes:
    with open(file=config_file_path, mode="rb") as binary_file:
        binary_data: bytes = binary_file.read()
        return binary_data


def insert_spaces_in_hex(hex_str):
    return " ".join(hex_str[i : i + 2] for i in range(0, len(hex_str), 2))


def compare_binary_files():
    binary_data1 = read_config_file(ORIGINAL_CONFIG_PATH)
    binary_data2 = read_config_file(EDITED_CONFIG_PATH)

    chunk_size = 16  # Set the chunk size to 16 bytes

    chunks1 = [
        binary_data1[i : i + chunk_size]
        for i in range(0, len(binary_data1), chunk_size)
    ]
    chunks2 = [
        binary_data2[i : i + chunk_size]
        for i in range(0, len(binary_data2), chunk_size)
    ]

    # Compare the chunks
    diff = []
    for i, (chunk1, chunk2) in enumerate(zip(chunks1, chunks2)):
        if chunk1 != chunk2:
            diff.append((i, chunk1, chunk2))

    return diff


def main():
    diff = compare_binary_files()

    if not diff:
        print("No differences found between the files.")
    else:
        for i, chunk1, chunk2 in diff:
            print(f"\n\nDifference found in Chunk {i}:")
            print(f"Original Chunk:\n{insert_spaces_in_hex(chunk1.hex())}")
            print(f"Edited Chunk:\n{insert_spaces_in_hex(chunk2.hex())}")


if __name__ == "__main__":
    main()
