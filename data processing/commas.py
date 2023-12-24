file_path = r"C:\Users\****\Documents\formatting.txt"

# Read the contents of the file and modify each line
with open(file_path, 'r') as file:
    lines = file.readlines()

# Add a comma at the end of each line
lines_with_comma = [line.strip() + ',' for line in lines]

# Write the modified lines back to the file
with open(file_path, 'w') as file:
    file.writelines('\n'.join(lines_with_comma))

print("Comma added at the end of every line in the file.")
