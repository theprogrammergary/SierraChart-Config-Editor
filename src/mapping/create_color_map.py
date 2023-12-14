import json
import random

# Generate 370 unique hexadecimal color codes
color_mapping = {}
while len(color_mapping) < 370:
    color_code = "".join(random.choice("0123456789ABCDEF") for _ in range(6))
    if color_code not in color_mapping.values():
        color_mapping[str(len(color_mapping) + 1)] = color_code

# Specify the filename for the JSON file
json_filename = "color_map.json"

# Write the color mappings to the JSON file
with open(json_filename, "w") as json_file:
    json.dump(color_mapping, json_file, indent=4)

print(f"Color mappings have been saved to {json_filename}")
