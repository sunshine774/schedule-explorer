import os

folder_path = r'C:\Users\a\Downloads\alessverloren-main\alessverloren-main\data5'

def remove_first_and_last_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Remove first and last lines
    modified_lines = lines[1:-1]

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

def process_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):  # Adjust the file extension if needed
            file_path = os.path.join(folder_path, filename)
            remove_first_and_last_line(file_path)

if __name__ == "__main__":
    process_files_in_folder(folder_path)
