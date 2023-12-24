import os
import json

# Function to parse a line and convert it to the desired format
def parse_line(line):
    parts = line.strip().split(', ')
    if len(parts) == 4:
        date, time, room, class_info = parts
        return {
            "date": date,
            "time": time,
            "room": room,
            "class": class_info
        }
    else:
        return None

# Input and output directory paths
input_dir = "C:\\Users\\*\\Documents\\git\\output"
output_dir = "C:\\Users\\*\\Documents\\git\\output2"

# Process each text file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, filename.replace(".txt", ".json"))

        formatted_data = []
        
        with open(input_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parsed_data = parse_line(line)
                if parsed_data:
                    formatted_data.append(parsed_data)

        with open(output_file, 'w') as json_file:
            json_file.write(json.dumps(formatted_data, indent=4))
