"""
Script to quickly change a color setting for the 20 sierra chart
global graphics configs in Sierra4.config
"""
import os

FILE_PATH: str = "C:\\Trading Software\\TPH-Sierra-Chart\\Sierra Chart\\Sierra4.config"

SEARCH_SEQUENCE: bytes = bytes.fromhex("F7 0A 54 00 14 00 04 00")
hex_string = "FF 80 FF 00"
CHANGES: list[bytes] = [bytes.fromhex(hex_string) for _ in range(20)]


def read_and_modify_binary_file(file_path, search_sequence, changes) -> None:
    """
    Changes a Sierra4.config file bytes.
    Finds a header position and then updates the color for
    each of the 20 global graphic configs

    Args:
        file_path (_type_): _description_
        search_sequence (_type_): _description_
        changes (_type_): _description_
    """

    with open(file=file_path, mode="rb") as file:
        binary_data: bytes = file.read()

    # Find the position of the search sequence
    position: int = binary_data.find(search_sequence)

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
        with open(file=file_path, mode="wb") as file:
            file.write(binary_data)

        print("\n\nChanges applied successfully.")
    else:
        print("\n\nSearch sequence not found in the file.")


def main() -> None:
    read_and_modify_binary_file(
        file_path=FILE_PATH, search_sequence=SEARCH_SEQUENCE, changes=CHANGES
    )


if __name__ == "__main__":
    main()
