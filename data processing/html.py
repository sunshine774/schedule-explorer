input_file_path = r"C:\Users\a\Documents\key.txt"
output_file_path = r"C:\Users\a\Documents\htmlkey.txt"

with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

formatted_lines = []

for line in lines:
    date, value = line.strip().split(': ')
    formatted_lines.append(f'"{date}": "{value}",')

formatted_content = '\n'.join(formatted_lines)

with open(output_file_path, 'w') as output_file:
    output_file.write(formatted_content)
