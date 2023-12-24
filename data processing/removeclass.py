import os

def remove_lines_with_prefix(file_path, prefix):
    # Read the original file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove lines starting with the specified prefix
    modified_lines = [line for line in lines if not line.startswith(prefix)]

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

def process_files_in_folder(folder_path, prefix_to_remove):
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the path is a file (not a directory)
        if os.path.isfile(file_path):
            # Apply the line removal logic to each file
            remove_lines_with_prefix(file_path, prefix_to_remove)

# Example usage
folder_path = r'C:\Users\h\Downloads\alessverloren-main\alessverloren-main\data1'
prefix_to_remove = 'The'  # Replace with the prefix you want to remove

process_files_in_folder(folder_path, prefix_to_remove)
