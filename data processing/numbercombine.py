def combine_numbers(input_file, output_file):
    combined_lines = []

    with open(input_file, 'r') as file:
        current_group = []
        for line in file:
            line = line.strip()
            if line == '-':
                if current_group:
                    combined_lines.append('_'.join(current_group))
                    current_group = []
                combined_lines.append('-')
            elif line.isdigit():
                current_group.append(line)
            else:
                combined_lines.append(line)

        if current_group:
            combined_lines.append('_'.join(current_group))

    combined_data = '\n'.join(combined_lines)

    with open(output_file, 'w') as output:
        output.write(combined_data)

# Input and output file paths
input_file_path = "C:\\Users\\a\\Documents\\git\\id2.txt"
output_file_path = "C:\\Users\\a\\Documents\\git\\hope.txt"

# Combine numbers and save to the output file
combine_numbers(input_file_path, output_file_path)
