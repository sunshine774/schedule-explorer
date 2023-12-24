import os

# Define input and output folder paths
input_folder_path = r"C:\Users\****\Documents\compass\!!teachersincluded\dtrct.txt"
output_folder_path = r"C:\Users\*****\Documents\compass\!!teachersincluded\FIXED"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Iterate through all text files in the input folder
for filename in os.listdir(input_folder_path):
    if filename.endswith(".txt"):
        # Construct input and output file paths for each file
        input_file_path = os.path.join(input_folder_path, filename)
        output_file_path = os.path.join(output_folder_path, f"{filename}")

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

        print(f"Modified content saved to {output_file_path}")
