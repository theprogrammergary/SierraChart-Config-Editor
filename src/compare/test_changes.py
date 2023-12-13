import os

# File path of the binary data file
FILE_PATH: str = "C:\\Trading Software\\TPH-Sierra-Chart\\Sierra Chart\\Sierra4.config"

# Search for this sequence of bytes
search_sequence = bytes.fromhex("1C 11 54 00 14 00 04 00")

# Define the changes to be made after the search sequence
changes = [
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
    bytes.fromhex("FF 80 FF 00"),  # Replace with FF 80 FF 00
]


def read_and_modify_binary_file(file_path, search_sequence, changes):
    with open(file_path, "rb") as file:
        binary_data = file.read()

    # Find the position of the search sequence
    position = binary_data.find(search_sequence)

    if position != -1:
        # Apply changes to the bytes following the search sequence
        for change in changes:
            binary_data = (
                binary_data[: position + len(search_sequence)]
                + change
                + binary_data[position + len(search_sequence) + len(change) :]
            )
            position += len(change)

        # Write the modified binary data back to the file
        with open(file_path, "wb") as file:
            file.write(binary_data)

        print("Changes applied successfully.")
    else:
        print("Search sequence not found in the file.")


def main():
    read_and_modify_binary_file(FILE_PATH, search_sequence, changes)


if __name__ == "__main__":
    main()
