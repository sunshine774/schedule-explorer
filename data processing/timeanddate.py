import os
from datetime import datetime

def get_day_from_date(date_str):
    # Convert date string to datetime object
    date_obj = datetime.strptime(date_str, '%d/%m')
    # Assuming all dates are in 2023
    date_obj = date_obj.replace(year=2023) # IMPORTANT, CHANGE TO CORRECT YEAR
    # Get the day name (Monday, Tuesday, etc.)
    day_name = date_obj.strftime('%A')
    return day_name

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if 'Date:' in line:
                # Extract the date from the line
                date_str = line.split('Date:')[1].strip()
                try:
                    # Get the day corresponding to the date
                    day_name = get_day_from_date(date_str)
                    # Write the original line and the 'Day:' line to the output file
                    outfile.write(line)
                    outfile.write(f'Day: {day_name}\n')
                except ValueError:
                    # Handle the case where the date is not in the expected format
                    print(f"Skipping line: {line.strip()} (Invalid date format)")
            else:
                outfile.write(line)

def process_files_in_folder(folder_path, output_folder):
    # List all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):  # Process only .txt files
            input_file_path = os.path.join(folder_path, filename)
            output_file_path = os.path.join(output_folder, f'output_{filename}')
            process_file(input_file_path, output_file_path)
            print(f"Processing complete for {filename}. Output written to {output_file_path}")

# Specify the folder path
folder_path = r'C:\Users\a\Downloads\alessverloren-main\alessverloren-main\data2'
output_folder = r'C:\Users\a\Downloads\alessverloren-main\alessverloren-main\data3'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process all files in the folder
process_files_in_folder(folder_path, output_folder)
