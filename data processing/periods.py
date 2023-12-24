time_mappings = {
    "08:35 AM": "Mentor",
    "09:30 AM": "Mentor",
    "08:50 AM": "Period 1",
    "09:50 AM": "Period 2",
    "11:15 AM": "Period 3",
    "12:15 PM": "Period 4",
    "02:00 PM": "Period 5",
    "09:35 AM": "Mentor",
    "08:55 AM": "Period 1",
    "12:30 PM": "Assembly",
    "03:00 PM": "Period 6",
    "09:55 AM": "Period 2",
    "09:40 AM": "Period 2",
    "10:50 AM": "Period 3",
    "11:40 AM": "Period 4",
    "02:10 PM": "Period 5"
}

def replace_times_in_file(input_file, output_file, time_mappings):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        for time, replacement in time_mappings.items():
            content = content.replace(time, replacement)

        with open(output_file, 'w') as file:
            file.write(content)

        print("Replacement completed successfully.")

    except FileNotFoundError:
        print("File not found.")

# Input and output file paths
input_file = r'C:\Users\******\Documents\git\hyphened.txt'
output_file = r'C:\Users\*****\Documents\git\periods.txt'

# Replace times in the input file and save the result to the output file
replace_times_in_file(input_file, output_file, time_mappings)
