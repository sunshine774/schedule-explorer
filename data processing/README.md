# Project Information

This project utilizes Python 3.11/3.10, though the version should not be a limiting factor.

- **VSCode Download:** [Download Visual Studio Code](https://code.visualstudio.com/download)

- **Python Download:** [Download Python](https://www.python.org/downloads/)

## Quick Start

1. Clone the repository and run the code or download .zip file.
2. Adjust paths as needed by copying them from the file explorer.

   Example Path: `C:\Users\USERNAME\Documents\example.txt`

3. Python extension in vscode will be useful.

## Data Processing Steps

### Who's in There?

[Video Tutorial](https://youtu.be/yUCWbcQ-zYk)

1. Run `cleanfolder.py` on the folder containing timetables saved as .txt files.
2. Use `filemerge.py` on the new folder.
3. Apply `fixmistake.py` on `MERGED.txt`.
4. Run `hyphens.py`.
5. Run `periods.py`.
6. Use `remover.py`.
7. Run `spaceremover.py`.
8. Apply `teach.py`.
9. Run `progressbaridder.py`. Note before running: You can edit the key.txt file as per my recommendations in the key.js file.
10. Run `numbercombine.py`.
11. Run `html11.py`.
12. Use `commas.py`.
13. Use `html.py` for the key to correct format.
14. Utilize `framework.html` to add the data.
15. Run `ids to names.py`.

**Note** Due to spelling and output conflicts the code doesnt work on one wednesday every fortnight. To fix this all that needs to be changed is removing every line with '9:30 AM' in it. Near these lines there may be lines that don't fit the expected format of "number_number_number": "output", these lines also need to be removed. This can be avoided by avoiding such conflicts in the key files.

**Note.** Changing the key needed for this code to run. It outlines steps with comments in the scripts and key files.
### Every Class' Schedule 7-10


[Video Tutorial](https://youtu.be/v1APKe6q4lg)

1. Run `cleanfolder.py` on the folder with timetable .txt files.
2. Use `fixmistakefolder.py`.
3. Run `formattingdata2folder.py`.
4. Split activities into class folders.
5. READ THE NOTE, THIS IS WHERE YOU USE IT.
6. Use `mergejson.py` for each class folder.
7. Insert into `classschedframework.html` following the provided instructions.
8. Run `ids to names.py` if necessary.

**Note**. For sport sessions (7-10) Make a duplicate of the same file for every single class. This will make sure full year sport is included on the correct day. You can also do this for years 9 and 10 mathematics. Use the script for one maths class and duplicate it into every 9/10 class, however due to how mathematics classes are changing in 2024 this option may not be viable. For electives (9 and 10) you can find two elective classes (preferably the same subject but different classes, eg. 9 Commerece 1 and 9 Commerce 2). This is because elective classes are on 'lines' and for electives there are two different lines. Lines meaning when they occur, For example 'line a' may have a commerece class on monday p1 and tuesday p3 and p4 and 'line 2' has classes on wednesday p1 and p2 and thursday p5. But regardless of which line for a class they fall under, the whole year grade has electives concurrently. So just find two elective subjects that dont have matching timetables. Then run the script on them, duplicate them both and put them in each class folder for the respective grades.
For years 7 and 8 it works similarly, when one class has technology every single other class in the year grade has either technology, art or music. However technology goes on the whole year but art/music goes on for half a year each. So we need to extract timetables from 3 subjects but the same class. Find 7/8 VA 1 and 7/8 TECH 1 and 7/8 MUSIC 1 (va, tech and mus classes have the same people therefore this covers all lines). Run the script on them and distrive across the respective grade folders.

I made a script its named `electmustec.py` that will help with this. Once you have a original file for every line run the code on every file individually. Make sure to edit the file apporpriatly depending on the subject. Once you have ran the script on all the y7 and y8 music, art and tech files, the y9 and y10 elective and maths files. and the 7-10 sport files. Make duplicates for every class in the grade of the given file and insert it into the folder made.

#### Steps
Sport: Collect one sport session from each year grade and put them in a folder. Lets say they are named 7 Sport A, 8 Sport A, 9 Sport A and 10 Sport A. In the script file edit the path to the 7 Sport A .json file, then in line 17 in the beginning it says '8 Music 4', Change that with what the file is named, in this case 7 Sport A. In line 18 replace New Desired Text with in this case 7 Sport. Do this for the rest of the grades.

Do this for the following:
Year 9 and 10 electives in 'New Desired Text' Elective, Year 9 and 10 mathematics in 'New Desired Text' put Mathematics, year 7 and 8 music, tech and va, in 'New Desired Text' just put 'year grade' TAS.



### Teacher's Schedules

[Video Tutorial](https://youtu.be/4aqmf3DgraI)

1. Run `cleanfolder.py` on the folder with timetable .txt files.
2. Use `filemerge.py` on the new folder.
3. Apply `fixmistake.py` on `MERGED.txt`.
4. Use `formatdtrct.py`.
5. Run `format1.py`.
6. Use `removenames.py`.
7. Run `jsonformattingfolder.py`.
8. Organize into `classschedframework.html`, using capitals for names.

**Note.** There will be some duplicate json with the teacherID with a comma, this means multiple teachers were rostered for one activity. Due to how uncommon this is, it is best just to ignore them. They are also typically mentor classes. 
### Subject Weekly Schedule

[Video Tutorial](https://youtu.be/wKWOOhBcq9c)

1. Run `cleanfolder.py`.
2. Use `removeclass.py`.
3. Run `fixmistakefolder.py`.
4. Use `timedatefolder.py`. Note. Make sure the correct year is on line 8.
5. Run `hyphenfolder.py`.
6. Use `jsonmaker.py`.
7. Run `rename.py`.
8. Use `activityaddjson.py`.
9. Run `removecurlybrackets.py`.
10. Use `addcommas.py`.
11. Run `mergedjson.py`.
12. Paste the file into `classsubjectsw.html`.
13. Find and replace 'Term 1-4' with 'Term1-4' in hierarchical JSON.
14. Run `IDS to names.py`.

## Extra Tools

[Video Tutorial](https://youtu.be/-0eti9Rt5Jk)

- Use `roomlist.py` to show all rooms in a file if it contains 'Room:'. `fixmistake.py` or `fixmistake.py` has to be ran before running this file.
- Use `listIDS.py` to show all teacherIDS in a file if it contains 'Teacher:'. `fixmistake.py` or `fixmistake.py` has to be ran before running this file.
- `key.txt` is essential for running some scripts; edit as needed for rooms and periods.
- `default.txt` has a list of names in HTML format ready to paste; add as needed.
- `key.html` is necessary for 'Who's in There'; edit if required, and adjust `key.txt` accordingly.
- `termdates.py` is useful for `jsonmaker.py`; get start and end dates for the term to determine the week range.
- `listfiles.py` lists the name of every file in a folder without the file extension. This is useful for Subject Weekly Schedules to allow us to see all the options.
