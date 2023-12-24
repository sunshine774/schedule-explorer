import os

# Directory containing the .txt files
input_folder = "C:\\Users\\*****\\Documents\\compass\\!!teachersincluded\\FIXED"
output_folder = "C:\\Users\\*****\\Documents\\compass\\!!teachersincluded\\!FIXED"

# Create the output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, "filter_" + filename)

        # Open the input file for reading
        with open(input_file_path, 'r') as input_file:
            # Read all lines from the input file, excluding lines containing 'The class'
            filtered_lines = [line for line in input_file if 'The class' not in line]

        # Open the output file for writing
        with open(output_file_path, 'w') as output_file:
            # Write the filtered lines to the output file
            output_file.writelines(filtered_lines)

        print(f"Filtered content from {input_file_path} written to {output_file_path}")
