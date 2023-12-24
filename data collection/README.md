# Data Collection for Timetables

Automating this process may not be practical unless regular updates are needed, as it requires substantial effort. Here's a general outline for manual data collection:

Watch the [video tutorial](https://youtu.be/dq_xU9plFxM) for an overview of the timetable collection process.

For `updown.py` navigate to the directory with the script in it then run `pip install -r requirements.txt`, or run `pip install keyboard` in the terminal.

## Timetable Collection Steps:

1. Utilize `updown.py` to facilitate easier traversal of subjects; starting from the lowest subject id of the given year is easier.
2. Manually collect every timetable from every subject with respect to the steps in the video.

All activity text files should be saved in the same folder.

I recommend saving all the subjectID links somewhere incase you need to go back for whatever reason.

Don't include periods '.' eg, 9 mathematics 5.3.1 should be 531 instead.

For ease of use, when naming files with long activity names, use acronyms. E.g., "10 Physical Activity and Sport Studies 1" should be "10 PASS 1," and "11 Community and Family Studies 1" should be "11 CAFS 1." The main reason for simplifying the names is Subject Weekly Schedules; entering these long inconsistent names is annoying. However the full names can still be used if desired.

Year 11 and 12 subjects can be split into 2 categories, 1 unit and 2 units. One unit subjects are all non-ATAR, such as SiCT and EEC, and two unit courses are mainly ATAR courses with some exceptions, such as mathematics standard 1. The reason for mentioning this is there are some subjects with different amounts of units but are fundamentally the same subject. For example, SOR with 4 one unit classes (y11 2023) and 2 two unit classes. For such subjects, we include the amount of units in the file name. Example: "11 Studies of Religion 1 Unit 3," "11 Studies of Religion 2 Unit 2." However, the number of subjects with classes like this is low; they include SPL and SOR. Other subjects should only have either one or two unit classes. Hence the amount of units do not need to be mentioned, Example "11 Exploring Early Childhood 1 Unit," in this, it can be named "11 EEC" since there is only one class.

List of Acronyms:
- EEC: Exploring Early Childhood
- SPL/SLR: Sport, Lifestyle and Recreation
- SOR: Studies of Religion
- SiCT: Studies in Catholic Thought
- CAFS: Community and Family Studies
- PASS: Physical Activity and Sport Studies
- PVD/PDM: Photography & Digital Media
- ITT: Industrial Technology Timber
- DAT: Design and Technology
- SAC: Society and Culture
- HSIE: Human Society & its Environment
- PDHPE: Personal Development Health and Physical Education
- ITM: Industrial Technology Multimedia

**Note:** The decision to automate this process should be based on the frequency of updates and the effort required.

**Caution:** While automation may be efficient for regular updates, consider the trade-offs and assess whether the effort is justified for your specific use case.
