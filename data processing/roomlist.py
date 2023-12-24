file_path = r'C:\Users\*******\Documents\3Schedule for every class\COMPLETE.txt'

# Function to extract rooms from the file
def extract_rooms(file_path):
    unique_rooms = set()
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('Room:'):
                room = line.strip().split(': ')[1]
                unique_rooms.add(room)
    return unique_rooms

# Print unique rooms
unique_rooms = extract_rooms(file_path)
print('Unique Rooms:')
for room in unique_rooms:
    print(room)
