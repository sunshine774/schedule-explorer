import os

def list_files_without_extension(folder_path):
    try:
        # Get a list of all files in the folder
        files = os.listdir(folder_path)

        # Iterate through each file and print its name without extension
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            print(file_name)

    except FileNotFoundError:
        print("The specified folder path was not found.")

# Replace 'your_folder_path' with the actual path of your folder
folder_path = r'C:\Users\b\Documents\schedule-explorer\data\Year 7'
list_files_without_extension(folder_path)
