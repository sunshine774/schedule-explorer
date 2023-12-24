def process_file(file_path, keywords_to_remove, class_keyword, replacement_text):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove lines containing specified keywords
    modified_lines = [line for line in lines if not any(keyword in line for keyword in keywords_to_remove)]

    # Replace lines containing the specified class keyword
    modified_lines = [line.replace(class_keyword, replacement_text) if class_keyword in line else line for line in modified_lines]

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

if __name__ == "__main__":
    file_path = r"C:\Users\x\Downloads\data3s\8 Music 4.json"
    keywords_to_remove = ["room", "teacher"]
    class_keyword = '"class": "8 Music 4",' # this is what is says in the original file example is given
    replacement_text = '"class": "New Desired Text"' # change to general subject that is not class specific. For sport just replace it with 7-10 Sport, for 7/8 music, tech and art replace it with 7/8 TAS, for elective just put Elective.

    process_file(file_path, keywords_to_remove, class_keyword, replacement_text)

    print(f"Lines containing {keywords_to_remove} removed and class line modified in {file_path}.")
