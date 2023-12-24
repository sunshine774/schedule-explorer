input_file_path = r'C:\Users\*****\Documents\input.txt'
output_file_path = r'C:\Users\*****\Documents\hyphened.txt'

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        if line.strip():  # Check if the line is not empty
            output_file.write(line)
        else:
            output_file.write("-\n")

print(f"Hyphens added to empty lines. Result saved to {output_file_path}")
