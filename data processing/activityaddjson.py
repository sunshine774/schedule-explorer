import json
import os

folder_path = r"C:\Users\a\Downloads\alessverloren-main\alessverloren-main\data5"

# List all files in the folder
files = os.listdir(folder_path)

for file_name in files:
    # Check if the file is a JSON file
    if file_name.endswith(".json"):
        file_path = os.path.join(folder_path, file_name)

        # Open the JSON file for reading
        with open(file_path, 'r') as file:
            # Load the JSON data
            data = json.load(file)

        # Create the new key without the ".json" extension
        prefix = file_name[:-5].upper()  # Remove the last 5 characters (".json") and convert to uppercase

        # Add the filename in uppercase as a prefix to the data
        prefixed_data = {prefix: data}

        # Open the same file for writing
        with open(file_path, 'w') as file:
            # Write the modified data back to the file
            json.dump(prefixed_data, file, indent=2)

        print(f"Added filename in uppercase as a prefix to {file_name}")
