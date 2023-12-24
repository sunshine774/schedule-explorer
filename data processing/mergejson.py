import os
import json

input_folder = r"C:\Users\****\Documents\compass\formatted_files_json\10E"
output_file = r"C:\Users\******\Documents\compass\formatted_files_json\!merged\10E.json"

data_list = []

for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        file_path = os.path.join(input_folder, filename)

        with open(file_path, 'r') as json_file:
            data_list.extend(json.load(json_file))

with open(output_file, 'w') as merged_json_file:
    json.dump(data_list, merged_json_file, indent=4)

print("Merging complete.")
