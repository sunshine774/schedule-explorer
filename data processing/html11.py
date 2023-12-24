input_file_path = "C:\\Users\\x\\Documents\\git\\hope.txt"
output_file_path = "C:\\Users\\x\\Documents\\git\\longshot.txt"

output_data = {}  # Dictionary to store the formatted data

with open(input_file_path, "r") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    if lines[i].strip() == "-":
        i += 1
        continue

    key = lines[i + 1].strip()
    value = lines[i].strip()
    output_data[key] = value

    i += 2

with open(output_file_path, "w") as f:
    for key, value in output_data.items():
        f.write(f'"{key}": "{value}"\n')
