import os

def combine_text_files(folder_path, output_file):
    # Get a list of all text files in the folder
    text_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

    # Open the output file for writing
    with open(output_file, 'w') as output:
        # Iterate through each text file and append its contents to the output file
        for text_file in text_files:
            file_path = os.path.join(folder_path, text_file)
            with open(file_path, 'r') as input_file:
                output.write(input_file.read())
                output.write('\n')  # Add a newline between the contents of different files

    print(f"Combination complete. Output saved to {output_file}")

# Specify the folder containing the text files and the output file
folder_path = r'C:\Users\*\Downloads\alessverloren-main\alessverloren-main\data5'
output_file = r'C:\Users\*\Downloads\alessverloren-main\alessverloren-main\data5\!MERGED.txt'
# Call the function to combine the text files
combine_text_files(folder_path, output_file)
