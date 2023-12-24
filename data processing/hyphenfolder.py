import os

def add_hyphen_for_empty_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Check if the line is empty (contains only whitespace characters)
            if not line.strip():
                outfile.write('-\n')  # Add a hyphen for empty lines
            else:
                outfile.write(line)

def process_files_in_folder(folder_path, output_folder):
    # List all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):  # Process only .txt files
            input_file_path = os.path.join(folder_path, filename)
            output_file_path = os.path.join(output_folder, f'output_{filename}')
            add_hyphen_for_empty_lines(input_file_path, output_file_path)
            print(f"Processing complete for {filename}. Output written to {output_file_path}")

# Specify the folder path
folder_path = r'C:\Users\x\Downloads\alessverloren-main\alessverloren-main\data3'
output_folder = r'C:\Users\x\Downloads\alessverloren-main\alessverloren-main\data4'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process all files in the folder
process_files_in_folder(folder_path, output_folder)
