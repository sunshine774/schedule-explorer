import os

# Folder path for merging the text files
merge_folder_path = r'C:\Users\****\Documents\compass\inputfoldername'

# Output file path for the merged content
output_file_path = os.path.join(merge_folder_path, 'MERGED.txt')

# List to store the content of all text files
merged_content = []

# Iterate through each file in the merge folder
for file_name in os.listdir(merge_folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(merge_folder_path, file_name)
        with open(file_path, 'r') as file:
            # Read the content of each file and append to the merged content list
            content = file.read()
            merged_content.append(content)

# Join the content of all files with a separator (e.g., newline)
merged_content_text = '\n'.join(merged_content)

# Write the merged content to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(merged_content_text)

print(f"Merged content written to {output_file_path}")
