def remove_spaces_at_start(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    # Remove spaces at the start of each line
    modified_lines = [line.lstrip() for line in lines]

    with open(output_file_path, 'w') as output_file:
        output_file.write(''.join(modified_lines))

if __name__ == "__main__":
    input_file_path = "C:\\Users\\******\\Documents\\git\\removed.txt"
    output_file_path = "C:\\Users\\******\\Documents\\git\\spaced.txt"

    remove_spaces_at_start(input_file_path, output_file_path)
