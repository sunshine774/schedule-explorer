# Define input and output file paths
input_file_path = r"C:\Users\*****\Documents\git\cleaned.txt\MERGED.txt"
output_file_path = r"C:\Users\******\Documents\git\MERGED2.txt"

# Read the input file
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

# Define the prefix to identify the objects to remove
prefixes = ["Room:", "Teacher:"]

# Initialize the output text
output_lines = []

# Iterate through the lines and process them
for line in lines:
    modified_line = None
    for prefix in prefixes:
        if line.startswith(prefix):
            # Split the line by whitespace
            parts = line.split()
            # Take the first part and create a modified line
            modified_line = f"{prefix} {parts[1]}\n"
            break
    if modified_line:
        output_lines.append(modified_line)
    else:
        # Preserve other lines
        output_lines.append(line)

# Write the modified content to the output file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(output_lines)

print("Modified content saved to", output_file_path)
