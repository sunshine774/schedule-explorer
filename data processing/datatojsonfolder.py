import os
import re
import json

# Function to convert text to JSON format
def convert_to_json(text):
    sections = re.split(r'\n\n', text.strip())
    result = []

    field_mapping = {
        "Date:": "date",
        "Time:": "time",
        "Room:": "room",
        "Teacher:": "class"
    }

    for section in sections:
        entry = {}
        lines = section.strip().split('\n')
        for line in lines:
            key, value = re.split(r':\s*', line, 1)
            entry[field_mapping.get(key, key)] = value
        result.append(entry)

    return json.dumps(result, indent=4)

# Input and output folder paths
input_folder = "C:\\Users\\*****\\Documents\\compass\\!!teachersincluded\\!FIXED"
output_folder = "C:\\Users\\******\\Documents\\compass\\!!teachersincluded\\!!FIXED"

# Ensure the output directory exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all .txt files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, "output_" + filename)

        # Read content from the input file
        with open(input_file_path, 'r') as input_file:
            input_text = input_file.read()

        # Convert the input text to JSON format
        json_output = convert_to_json(input_text)

        # Write the JSON content to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(json_output)

        print(f"Conversion complete for {input_file_path}. Result saved to {output_file_path}")
