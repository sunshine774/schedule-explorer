input_file_path = r"C:\Users\*****\Documents\git\MERGED2.txt"
output_file_path = r"C:\Users\*****\Documents\git\test.txt"

with open(input_file_path, 'r') as file:
    lines = file.read().split('\n\n')

output_lines = []

for group in lines:
    group_lines = group.split('\n')

    date = time = room = class_info = teacher = ""

    for line in group_lines:
        if "Date:" in line:
            date = line.split(': ')[1]
        elif "Time:" in line:
            time = line.split(': ')[1]
        elif "Room:" in line:
            room = line.split(': ')[1]
        elif "The class is" in line:
            class_info = line.split('The class is ')[1]
        elif "Teacher:" in line:
            teacher = line.split(': ')[1]

    output_line = f"{date}, {time}, {room}, {class_info}, {teacher}"
    output_lines.append(output_line)

with open(output_file_path, 'w') as output_file:
    for line in output_lines:
        output_file.write(line + '\n')
