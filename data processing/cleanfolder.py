import re
import os

def extract_info_from_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        lines = input_file.readlines()

        blocks = []
        current_block = []
        for line in lines:
            if line.strip():
                current_block.append(line.strip())
            elif current_block:
                blocks.append(current_block)
                current_block = []

        for block in blocks:
            date_match = re.search(r'(\d{2}/\d{2}) - (\d{2}:\d{2} [APap][Mm])', block[0])
            if date_match:
                date = date_match.group(1)
                time = date_match.group(2)
            else:
                date = "Date not found"
                time = "Time not found"

            room = block[2] if len(block) > 2 else "Room not found"
            teacher = block[3] if len(block) > 3 else "Teacher not found"

            # Extract the file name without the extension from the input_file_path
            file_name = os.path.splitext(os.path.basename(input_file_path))[0]

            output_file.write(f"Date: {date}\n")
            output_file.write(f"Time: {time}\n")
            output_file.write(f"Room: {room}\n")
            output_file.write(f"Teacher: {teacher}\n")
            output_file.write(f"The class is {file_name}\n\n")

def process_files_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".txt"):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(output_folder, f"{file_name}")
            extract_info_from_file(input_file_path, output_file_path)

if __name__ == '__main__':
    input_folder = r'C:\Users\******\Documents\rawdata'
    output_folder = r'C:\Users\*****\Documents\processing'
    process_files_in_folder(input_folder, output_folder)
