# Define the file path
file_path = "C:\\Users\\****\\Documents\\compass\\!!teachersincluded\\teachercleanedup\\Periods_added_fixed.txt"

# Initialize a set to store unique texts
unique_texts = set()

# Open the file and read its contents
with open(file_path, 'r') as file:
    for line in file:
        if 'Teacher:' in line:
            # Split the line by 'Teacher:'
            parts = line.split('Teacher:')
            if len(parts) > 1:
                text = parts[1].strip()  # Get the text after 'Teacher:' and remove leading/trailing whitespace
                unique_texts.add(text)  # Add the text to the set of unique texts

# Print the unique texts
for text in unique_texts:
    print(text)
