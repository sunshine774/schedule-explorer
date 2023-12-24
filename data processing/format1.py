# Input file path
input_file_path = r"C:\Users\a\Documents\git\!process2.txt"

# Read input data from the input file
with open(input_file_path, "r") as input_file:
    data = input_file.read()

# Split the data into lines
lines = data.strip().split('\n')

# Create a dictionary to store lines by teacher
teacher_lines = {}

# Iterate through the lines and sort them by teacher
for line in lines:
    parts = line.split(", ")
    teacher = parts[-1]
    if teacher not in teacher_lines:
        teacher_lines[teacher] = []
    teacher_lines[teacher].append(line)

# Create a separate text file for each teacher
for teacher, lines in teacher_lines.items():
    output_file_path = f"C:\\Users\\*****\\Documents\\git\\output\\{teacher}.txt"
    with open(output_file_path, "w") as output_file:
        output_file.write("\n".join(lines))

print("Files created and sorted successfully.")
