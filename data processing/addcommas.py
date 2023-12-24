import os

def add_comma_to_last_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Add a comma next to the square bracket on the last line
    last_line = lines[-1]
    last_line_with_comma = last_line.rstrip() + ','

    # Replace the last line in the list
    lines[-1] = last_line_with_comma

    with open(filename, 'w') as file:
        file.writelines(lines)

directory_path = r'C:\Users\x\Downloads\alessverloren-main\alessverloren-main\data5'

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.json'):  # Modify this condition based on your file type
        file_path = os.path.join(directory_path, filename)
        add_comma_to_last_line(file_path)

print("Modification complete.")
