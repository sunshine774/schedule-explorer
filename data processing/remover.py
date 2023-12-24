def remove_labels(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    # Remove labels 'Date:', 'Time:', 'Room:' from each line
    modified_lines = [line.replace('Date:', '').replace('Time:', '').replace('Room:', '').replace('Teacher:', '') for line in lines]

    with open(output_file_path, 'w') as output_file:
        output_file.write(''.join(modified_lines))

if __name__ == "__main__":
    input_file_path = "C:\\Users\\*****\\Documents\\git\\periods.txt"
    output_file_path = "C:\\Users\\******\\Documents\\git\\removed.txt"

    remove_labels(input_file_path, output_file_path)
