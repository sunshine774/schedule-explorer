import json
from datetime import datetime
import os

# Specify the folder containing the input files
input_folder = r"C:\Users\b\Downloads\alessverloren-main\alessverloren-main\data4"

# Specify the output folder for the JSON files
output_folder = r"C:\Users\b\Downloads\alessverloren-main\alessverloren-main\data5"

# Iterate over each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        # Construct the full file paths
        file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, f"{filename.split('.')[0]}_output.json")

        try:
            # Read data from the file
            with open(file_path, 'r') as file:
                content = file.read()

            # Split the content into individual sets
            sets = content.split('-\n')

            # Filter out empty sets (if any)
            sets = [data_set.strip() for data_set in sets if data_set.strip()]

            # Sort the sets based on date (assuming 'Date' is one of the keys in each set)
            sorted_data = sorted(sets, key=lambda x: datetime.strptime(x.split('\n')[0].split(': ')[1], '%d/%m') if len(x.split('\n')) > 0 else datetime.min)

            # Define the date ranges for each term and week
            term_weeks = {
                'Term 1': [
                    '27/01 - 02/02', '03/02 - 09/02', '10/02 - 16/02', '17/02 - 23/02', # THESE DAYS MAY NEED TO BE CHANGED CHECK TOOLS SECTION
                    '24/02 - 02/03', '03/03 - 09/03', '10/03 - 16/03', '17/03 - 23/03', # THESE DAYS MAY NEED TO BE CHANGED CHECK TOOLS SECTION
                    '24/03 - 30/03', '31/03 - 06/04' # THESE DAYS MAY NEED TO BE CHANGED CHECK TOOLS SECTION
                ],
                'Term 2': [
                    '24/04 - 30/04', '01/05 - 07/05', '08/05 - 14/05', '15/05 - 21/05', # THESE DAYS MAY NEED TO BE CHANGED CHECK TOOLS SECTION
                    '22/05 - 28/05', '29/05 - 04/06', '05/06 - 11/06', '12/06 - 18/06', # THESE DAYS MAY NEED TO BE CHANGED CHECK TOOLS SECTION
                    '19/06 - 25/06', '26/06 - 02/07' # THESE DAYS MAY NEED TO BE CHANGED CHECK TOOLS SECTION
                ],
                'Term 3': [
                    '17/07 - 23/07', '24/07 - 30/07', '31/07 - 06/08', '07/08 - 13/08', # THESE DAYS MAY NEED TO BE CHANGED CHECK TOOLS SECTION
                    '14/08 - 20/08', '21/08 - 27/08', '28/08 - 03/09', '04/09 - 10/09', # THESE DAYS MAY NEED TO BE CHANGED CHECK TOOLS SECTION
                    '11/09 - 17/09', '18/09 - 24/09' # THESE DAYS MAY NEED TO BE CHANGED CHECK TOOLS SECTION
                ],
                'Term 4': [
                    '09/10 - 15/10', '16/10 - 22/10', '23/10 - 29/10', '30/10 - 05/11', # THESE DAYS MAY NEED TO BE CHANGED CHECK TOOLS SECTION
                    '06/11 - 12/11', '13/11 - 19/11', '20/11 - 26/11', '27/11 - 03/12', # THESE DAYS MAY NEED TO BE CHANGED CHECK TOOLS SECTION
                    '04/12 - 10/12', '11/12 - 17/12', '18/12 - 24/12' # THESE DAYS MAY NEED TO BE CHANGED CHECK TOOLS SECTION
                ]
            }

            # Create a list to store the final JSON structure
            json_data = []

            # Iterate through each data set in the sorted_data
            for data_set in sorted_data:
                # Extract relevant information from the data set
                date_str = data_set.split('\n')[0].split(': ')[1]

                # Parse the date string to a datetime object
                date = datetime.strptime(date_str, '%d/%m')

                # Determine the term and week based on the date ranges
                term = None
                week = None
                for t, weeks in term_weeks.items():
                    for w, date_range in enumerate(weeks, start=1):
                        start_date, end_date = map(lambda x: datetime.strptime(x, '%d/%m'), date_range.split(' - '))
                        if start_date <= date <= end_date:
                            term = t
                            week = f'Week{w}'
                            break
                    if term:
                        break

                # Create a day's schedule object
                day_schedule = {
                    "day": data_set.split('\n')[1].split(': ')[1],
                    "time": data_set.split('\n')[2].split(': ')[1],
                    "room": data_set.split('\n')[3].split(': ')[1],
                    "teacher": data_set.split('\n')[4].split(': ')[1]
                }

                # Find the term object in the JSON data list or create a new one
                term_object = next((term_obj for term_obj in json_data if term_obj['term'] == term), None)
                if not term_object:
                    term_object = {"term": term, "data": []}
                    json_data.append(term_object)

                # Find the week object in the term's data list or create a new one
                week_object = next((week_obj for week_obj in term_object['data'] if week_obj['week'] == week), None)
                if not week_object:
                    week_object = {"week": week, "schedule": []}
                    term_object["data"].append(week_object)

                # Append the day's schedule object to the current week's schedule list
                week_object["schedule"].append(day_schedule)

            # Convert the final JSON data to a JSON-formatted string
            json_string = json.dumps(json_data, indent=2)

            # Create the output directory if it doesn't exist
            os.makedirs(output_folder, exist_ok=True)

            # Write the JSON string to the output file
            with open(output_file_path, 'w') as output_file:
                output_file.write(json_string)

            # Print a message indicating successful write for each file
            print(f"JSON data written to: {output_file_path}")

        except Exception as e:
            # Handle exceptions (e.g., file format not as expected)
            print(f"Skipping {file_path} due to error: {e}")
