import os

# Define the folder path
folder_path = r'C:\Users\*\Documents\git\output'

# Get a list of all TXT files in the folder
txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# Iterate through each TXT file
for txt_file in txt_files:
    file_path = os.path.join(folder_path, txt_file)
    file_name = os.path.splitext(txt_file)[0]  # Get the file name without the extension

    # Read the content of the TXT file
    with open(file_path, 'r') as file:
        content = file.read()

    # Remove all instances of the file name from the content
    content = content.replace(file_name, '')

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

print("Processing complete.")
