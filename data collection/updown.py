import keyboard
import webbrowser

base_url = "https://slccdbb-nsw.compass.education/Organise/Subjects/Subject.aspx?subjectId="
subject_id = 500     # this is the start subject ID

def open_subject():
    url = base_url + str(subject_id)
    webbrowser.open(url)

def increase_subject_id():
    global subject_id
    subject_id += 1
    open_subject()

def decrease_subject_id():
    global subject_id
    subject_id -= 1
    open_subject()

keyboard.add_hotkey('up', increase_subject_id)
keyboard.add_hotkey('down', decrease_subject_id)

open_subject()

keyboard.wait('esc')
