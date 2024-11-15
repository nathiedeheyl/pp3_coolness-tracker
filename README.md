# How to lower your resting heartbeat 

**Project Overview: Lower your resting heartbeat**  
This application is designed to help the user understand the correlation between cardiovascular exercise, mindful breathing exercises, and resting heartbeat. With the help of a smart wearable, the user can monitor their biodata. Our goal is to keep things cool: The lower the resting heartbeat, the more chill is life. With this application, the user will be able to find the ideal amount of cardio and breathing exercises to lower their resting heartbeat to a desired level by tracking biodata and exercise minutes over time. The user will also have the ability to run a command to gain insights into the current data trends.

**Key metrics** for this Python analysis are the user’s lowest heart rate during sleep, total minutes of cardiovascular exercise during the day, and total minutes of intentional breathing exercises.

**Main Goal:** Analyze correlations between the user’s heart rate, cardiovascular exercise, and relaxation practices to identify how fitness and relaxation impact the user’s resting heart rate.

## User stories 

**As a user …**
+ …I want a welcome message when I start the program that explains the purpose of the application and how it can benefit me.

+ …I want to easily understand how to input my data, so I can log my information without confusion or mistakes.

+ …I want clear, friendly prompts for each data entry, so I know exactly what is expected of me at each step.

+ …I want to be able to see a simple summary of my recent stats in one command, so I don’t have to look at long reports if I don’t want to.

+ …I want to be able to see if my resting heart rate is trending up or down.

+ …I want to understand how my cardio and relaxation practices impact my resting heart rate over time so that I keep up the healthy habits in order to lower it effectively.

+ …I want to log my daily lowest heart rate during sleep, total minutes of cardiovascular exercise, and total minutes of breathing exercises, so I can see the effect of my habits on my heart health over time.

+ …I want the program to notify me of the correct format and give me another chance to input valid data, if I input incorrect data (e.g., text instead of numbers etc.).

+ …I want the application to guide me back to the main input prompt after I make a mistake, so I can correct it easily without restarting.

+ …I want the analysis feedback to feel positive and helpful, highlighting any progress or improvements to keep me motivated.

+ …I want to receive a motivational message in the summary when I run an analysis, so I can feel encouraged to track my data daily and maintain consistentcy.

+ …I want a detailed view of correlations between my heart rate and my exercise and breathing practices to understand the effect of my health habits on the resting heartrate.

+ …I want to be able to exit the program smoothly and know that my data is saved, so I feel safe in using the application correctly and therefore trust the data analysis.

!!!
+ ...I want the application to allow me to skip logging on some days, without affecting my trend analysis, so I feel comfortable using it at my own pace.  

!!!

## Workflow 
![Process Flowchart](assets/images/python_program_flowchart_1.png)  
[Link to image in Google Drive for better resolution](https://drive.google.com/file/d/1ttHliz-kDCG_2PlvI5EhpljxHg-oFdWm/view?usp=drive_link)

<details>
<summary>Log of progress and notes (personal)</summary>
Set up:

1. Import Libraries: Bring in gspread to manage Google Sheets and Credentials for secure access.
2. Set Permissions with a Scope: Define what parts of Google Sheets and Drive the program is allowed to access.
3. Load Credentials: Use a creds.json file (generated when setting up API) to load the authorization key and apply the defined permissions.
4. Authorize and Open Sheet: Authorize access to Google Sheets with gspread, then open a specific sheet by name ('coolness_tracker' in my case).
</details>

## Features
<details>
<summary>List of features</summary>
• Welcome message and start menu
• Data validation: Regular resting heart rate [Source](https://www.mayoclinic.org/healthy-lifestyle/fitness/expert-answers/heart-rate/faq-20057979#:~:text=Answer%20From%20Edward%20R.%20Laskowski,to%20100%20beats%20per%20minute.); Maximum cardio minutes [Source](https://odphp.health.gov/our-work/nutrition-physical-activity/physical-activity-guidelines/current-guidelines/top-10-things-know) - But I decided to go a maximum input of 24h = 1.440 min. as for the breathwork minutes
</details>

## Testing
<details>
<summary>Bugs</summary>

| **Bug Description** | **Screenshot** | **Fix** | 
|---------------------|----------------|---------|
| print statement too long | ![flake8 validation issue 1](assets/images/testing/flake8_1.png) | Divided print statement in several lines |
| Error when inputtin uppercase or spaces in start menu | ![start menu input issue](assets/images/testing/bug_1.png) | add .strip() and .lower() methods to input field: ```instruction_choice = input("Do you need instructions? ").strip().lower()``` |
| Input upon main_menu redirects to start_menu instaed of displaying main_choice options | ![main menu input issue](assets/images/testing/bug_2.png) | add return statement to main_menu function; remove start_menu loop; comment out validate to proceed to main_menu after instructions; remove main_menu call from elif "no" to jump instructions; |
| health data input validation error | ![output on display error](assets/images/testing/bug_3.png) | put conversion ```int(heartrate_str)``` inside try/except code and wrap everything in a loop to give user a chance to put in right heartrate upon mistake |
</details>

## Credits 

<details>
<summary>Ressources</summary>
- YouTube tutorial on menus in python using a while true loop [Source](https://www.youtube.com/watch?v=ZBx7oWCJ4aY)
- To learn about more python methods, for input validation e.g.: [W3Schools](https://www.w3schools.com/python/ref_string_lower.asp)
</details>