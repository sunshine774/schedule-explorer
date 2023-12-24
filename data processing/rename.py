import os

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Remove 'output' and '_' from the filename
            new_filename = filename.replace('output', '').replace('_', '')
            
            # Rename the file
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f'Renamed: {filename} to {new_filename}')

# Replace 'path/to/your/folder' with the actual path to your folder
folder_path = r'C:\Users\a\Downloads\alessverloren-main\alessverloren-main\data5'
rename_files(folder_path)
