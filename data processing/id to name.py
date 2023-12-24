# Define the mapping of words to names
name_mapping = {
    "input": "output",
    "input": "output",
# add the rest
}

input_file_path = "C:\\Users\\c\\Documents\\compass\\!!teachersincluded\\UPDATED SCHEDULE.html"
output_file_path = "C:\\Users\\c\\Documents\\compass\\!!teachersincluded\\UPDATED SCHEDULE_final1.html"

# Read the input file and process its content
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

modified_lines = []

for line in lines:
    for word, name in name_mapping.items():
        line = line.replace(word, name)

    modified_lines.append(line)

# Write the modified content to the output file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(modified_lines)

print("Replacement completed. Modified content saved to Closer.txt.")
