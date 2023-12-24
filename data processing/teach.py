input_file_path = r"C:\Users\******\Documents\git\spaced.txt"
output_file_path = r"C:\Users\*****\Documents\git\id.txt"

with open(input_file_path, 'r') as file:
    lines = file.readlines()

output_lines = []
info_block = []

for line in lines:
    line = line.strip()  # Remove leading/trailing whitespace

    if line == '-':
        # Reached the end of an information block, process it
        if len(info_block) >= 5:
            # Append the 4th line to the end of the 5th line
            info_block[4] += f', The teacher is {info_block[3]}'
            # Remove the 4th line from the info_block
            info_block.pop(3)
            # Add the hyphen back to the output
            info_block.append('-')
            output_lines.extend(info_block)
        else:
            # If the block is incomplete, simply add it to the output
            output_lines.extend(info_block)
        info_block = []  # Reset the info_block list
    else:
        info_block.append(line)

# Write the modified content to a new file
with open(output_file_path, 'w') as file:
    file.write('\n'.join(output_lines))

print("Processing complete. Check 'FINAL2.txt' for the result.")
