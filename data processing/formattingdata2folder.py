import re
import json
import os

def get_class_name_from_filename(file_path):
    # Extract class name from the filename (without extension)
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    return file_name

def txt_to_json(txt_content, class_name):
    schedule = []
    current_entry = {}

    for line in txt_content:
        if line.startswith("Date:"):
            if current_entry:
                schedule.append(current_entry.copy())
            current_entry = {"date": "", "time": "", "room": "", "class": class_name, "teacher": ""}
            date_match = re.search(r"Date: (\d{2}/\d{2})", line)
            if date_match:
                current_entry["date"] = date_match.group(1)
        elif line.startswith("Time:"):
            time_match = re.search(r"Time: (\d{2}:\d{2} [APMapm]+)", line)
            if time_match:
                current_entry["time"] = time_match.group(1)
        elif line.startswith("Room:"):
            room_match = re.search(r"Room: (.+)", line)
            if room_match:
                current_entry["room"] = room_match.group(1)
        elif line.startswith("Teacher:"):
            teacher_match = re.search(r"Teacher: (.+)", line)
            if teacher_match:
                current_entry["teacher"] = teacher_match.group(1)

    if current_entry:
        schedule.append(current_entry)

    return schedule

def process_folder(input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".txt"):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(output_folder, f"{file_name.split('.')[0]}.json")

            class_name = get_class_name_from_filename(input_file_path)

            with open(input_file_path, "r") as file:
                txt_content = file.readlines()

            schedule_json = txt_to_json(txt_content, class_name)

            with open(output_file_path, "w") as json_file:
                json.dump(schedule_json, json_file, indent=2)

            print(f"Conversion completed for {file_name}. Output saved to '{output_file_path}'.")

if __name__ == "__main__":
    input_folder_path = r"C:\Users\aless\Documents\place\data2"
    output_folder_path = r"C:\Users\aless\Documents\data1\output"

    # Ensure the output folder exists
    os.makedirs(output_folder_path, exist_ok=True)

    process_folder(input_folder_path, output_folder_path)
