def replace_text(input_file, key_file, output_file):
    replacements = {}

    # Read the key file and create a dictionary for replacements
    with open(key_file, 'r') as key_file:
        for line in key_file:
            original_text, replace_with = line.strip().split(':')
            replacements[original_text.strip()] = replace_with.strip()

    # Read the input file, perform replacements, and write to the output file
    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
        total_lines = sum(1 for _ in input_file)  # Count total lines in the input file
        input_file.seek(0)  # Reset file pointer to the beginning

        for line_num, line in enumerate(input_file, start=1):
            for original_text, replace_with in replacements.items():
                if original_text in line:
                    line = line.replace(original_text, replace_with)
            output_file.write(line)
            
            # Calculate progress and print it
            progress = (line_num / total_lines) * 100
            print(f"Progress: {progress:.2f}% Complete", end='\r')

# Input and output file paths
input_file = "C:\\Users\\*****\\Documents\\git\\id.txt"
key_file = "C:\\Users\\*****\\Documents\\compass\\key.txt" # note before running in this repository there is a key.js file with recommendations on how to edit the key.txt file in order to make the code run more smoothly.
output_file = "C:\\Users\\******\\Documents\\git\\id2.txt"

# Replace text based on the key and write to the output file
replace_text(input_file, key_file, output_file)
print("Progress: 100.00% Complete")  # To indicate completion
