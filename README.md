# Coolness tracker

![Welcome message](assets/images/features/feature_1_welcome2.png)

An assistant for lowering your resting heartbeat and live a calmer life.
[Click here to access live project terminal](https://coolness-tracker-7669906b729c.herokuapp.com/).

## Overview 

**Project Overview: Lower your resting heartbeat**  
This application helps users explore the relationship between cardiovascular exercise, mindful breathing, and resting heart rate. By tracking three key metrics (lowest resting heart rate during sleep, daily cardio minutes, and mindful breathwork minutes) users can gain insights into how their habits impact their overall well-being - because the lower the resting heartbeat, the more chill is life.

The data entered is stored anonymously, and the option for last week's analysis provides a clear summary of trends to encourage a healthier, more relaxed lifestyle.

**Key metrics** for this Python analysis are the user’s lowest heart rate during sleep, total minutes of cardiovascular exercise during the day, and total minutes of intentional breathing exercises during one day.

**Main Goal:** Analyze the relationship between heart rate, cardiovascular activity, and relaxation practices to understand their impact on resting heart rate and overall well-being.

## Workflow 
<details>
<summary>Process flowcharts</summary>

<details>
<summary>Flowchart.1</summary>

![Process flowchart 1](assets/images/workflow/python_program_flowchart_1.png)

[Link to process flowchart 1 for higher resolution](https://drive.google.com/file/d/1WOr0uh1Km6rs3N1jSxBHXMMrOjg33fCc/view?usp=sharing)

</details>

<details>
<summary>Flowchart.2</summary>

![Process flowchart 1](assets/images/workflow/python_program_flowchart_2.png)

[Link to process flowchart 2 for higher resolution](https://drive.google.com/file/d/1FIiiGRFyn7p4dhGeM7953NLfwcWvprex/view?usp=sharing)

</details>
</details>

## User stories 

<details>
<summary>**As a user …**</summary>

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

</details>

## Deployment
Before deploying, ensure you've completed the following:
- Remove unnecessary imports used for testing that aren't needed in the final Heroku deployment.
- Add a line using `\n` after input statements for technical reasons.
- Update requirements.txt to include all dependencies using terminal command "pip3 freeze > requirements.txt"
- Sign up for a Heroku account and link it to GitHub.
- Add billing information to deploy and run apps on Heroku.

Deployment steps after setting up account on Heroku:
1. In the top-right corner of your Heroku Dashboard, click "New", then choose "Create new app" from the dropdown. (On first app deployment you'll see a button to select on the dashboard directly.)
2. Enter a unique name for your app, select the region you live in or that is closest to you (USA or EU), and click "Create App".
3. In your app’s Settings, select "Reveal Config Vars". Set "PORT" as the KEY and "8000" as the value, then click "Add".
4. Add another Config Var. Set "CREDS" as the KEY, copy the creds.json file in your workspace and paste it into the VALUE field, then click "Add".
5. Scroll down to the Buildpacks section and click "Add buildpack" to manage dependencies.
6. Ensure the buildpacks are in the correct order: Python first, followed by Node.js.
7. Navigate to the deploy section to choose deployment method.
8. Under "Deployment method", select "Github".
9. Confirm that you want to connect to Github. Sign in to Github via the pop-up window.
10. After confirming you can search for your Github repository name by typing in the name of your repository, click "Search", and finally, "Connect" to link up the Heroku app to your Github repository code.
11. Scroll down and navigate to "Deploy branch". Choose a branch to deploy. Optionally select "Enable Automatic Deploys".
12. After deployment is completed, you receive a message "Your app was successfully deployed." Select "View" to open your deployed link.
13. You will be automatically redirected to the running Mock Terminal.

See live Project Terminal here: https://coolness-tracker-7669906b729c.herokuapp.com/

See also [deployment documentation on Heroku's website](https://devcenter.heroku.com/articles/git). As well as [more information about cloning a Github repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

## Features

1. Start of the program

    • Welcome message and start menu

2. SOME FEATURE

    • Data validation: Regular resting heart rate [Source](https://www.mayoclinic.org/healthy-lifestyle/fitness/expert-answers/heart-rate/faq-20057979#:~:text=Answer%20From%20Edward%20R.%20Laskowski,to%20100%20beats%20per%20minute.); Maximum cardio minutes [Source](https://odphp.health.gov/our-work/nutrition-physical-activity/physical-activity-guidelines/current-guidelines/top-10-things-know) - But I decided to go a maximum input of 24h = 1.440 min. as for the breathwork minutes

### Future Features

- More detailed error handling on inputs: Individual error messages for empty inputs, negative number inputs, empty or whitespace inputs and so on.
- Implement 'exit' option during input.
- Handling invalid date format and skipping rows (unlikely to occur).
- Handling error message if spreadsheet/worksheet are unavailable/deleted.

## Testing

### Testing User Stories

| **User story** | **Evaluation** |
|----------------|----------------|
| - | - |

### Code validation

| **Check** | **Description of Issue** | **Screenshot** |
|----------------|---------------------|----------------|
| - | 221: E501 line too long | ![validation screenshot 1](assets/images/testing/validation_1.png) |
| - | 283: E501 line too long | ![validation screenshot 1](assets/images/testing/validation_2.png) |
| ✅ | All clear, no errors found | ![validation screenshot 1](assets/images/testing/validation_3.png) |

## Manual testing

| **validation** | **f(x)** | **description/expectation** | **comment** |
|----------------|----------|----------------|----------|
| ✅ | display_welcome_message() | display welcome message | . |
| ✅ | start_menu() | option: WRONG INPUT, random words, white space, enter | . |
| ✅ | start_menu() | option: yes | . |
| ✅ | start_menu() | option: yEs | . |
| ✅ | start_menu() | option: no | . |
| ✅ | start_menu() | option: nO_ | . |
| ✅ | start_menu() | option: x | . |
| ✅ | start_menu(): option: yes and proceed to MAIN MENU? | Any input to proceed | ENTER or any input and ENTER work to proceed to Main Menu |
| ✅ | main_menu() | option: x | prints statement and exits |
| ✅ | main_menu() | option: a | see: get_health_stats() |
| ✅ | main_menu() | option: b | see: calculate_avr_heartrate(); calculate_sum_cardio(); calculate_sum_breathwork() |
| ✅ | get_health_stats() | prompt for 3 entries | . |
| ✅ | get_health_stats() | error handling: wrong input | No input and ENTER is not accepted, white space is not accepted, error handling for ValueError works, error handling for out of num range works |
| ✅ | update_worksheets() | writes on Google sheet including timestamp in format yy-mm-dd | . |
| ✅ | update_worksheets() | displayes message of successful update of each worksheet | . |
| ✅ | calculate_avr_heartrate() | fetch all data from worksheet minus header | . |
| ✅ | calculate_avr_heartrate() | filter data for entries of last 7 days since today using datetime | . |
| ✅ | calculate_avr_heartrate() | validate there's data of last 7 days | . |
| ✅ | calculate_avr_heartrate() | calculate average and round to whole number | . |
| ✅ | calculate_avr_heartrate() | error handling for invalid input | . |
| ✅ | calculate_avr_heartrate() | output: message to user | . |
| ✅ | def calculate_sum_cardio() | fetch all data from worksheet minus header | . |
| ✅ | def calculate_sum_cardio() | filter data for entries of last 7 days since today using datetime | . |
| ✅ | def calculate_sum_cardio() | validate there's data of last 7 days | . |
| ✅ | def calculate_sum_cardio() | calculate sum and display hours and minutes using modulo | . |
| ✅ | def calculate_sum_cardio() | error handling for invalid input | . |
| ✅ | def calculate_sum_cardio() | output: message to user | . |
| ✅ | calculate_sum_breathwork | fetch all data from worksheet minus header | . |
| ✅ | calculate_sum_breathwork | filter data for entries of last 7 days since today using datetime | . |
| ✅ | calculate_sum_breathwork | validate there's data of last 7 days | . |
| ✅ | calculate_sum_breathwork | calculate sum | . |
| ✅ | calculate_sum_breathwork | error handling for invalid input | . |
| ✅ | calculate_sum_breathwork | output: message to user | . |
| ✅ | main() | back to MAIN MENU | works in all cases by pressing ENTER or any key and ENTER |
| ✅ | main() | exit() | works and displays output message to user |


### Bugs

| **Bug Description** | **Screenshot** | **Fix** | 
|---------------------|----------------|---------|
| print statement too long | ![flake8 validation issue 1](assets/images/testing/flake8_1.png) | Divided print statement in several lines |
| Error when inputtin uppercase or spaces in start menu | ![start menu input issue](assets/images/testing/bug_1.png) | add .strip() and .lower() methods to input field: ```instruction_choice = input("Do you need instructions? ").strip().lower()``` |
| Input upon main_menu redirects to start_menu instaed of displaying main_choice options | ![main menu input issue](assets/images/testing/bug_2.png) | add return statement to main_menu function; remove start_menu loop; comment out validate to proceed to main_menu after instructions; remove main_menu call from elif "no" to jump instructions; |
| health data input validation error | ![output on display error](assets/images/testing/bug_3.png) | put conversion ```int(heartrate_str)``` inside try/except code and wrap everything in a loop to give user a chance to put in right heartrate upon mistake |
| Use of wrong emoji leads to display of other symbols in deployed version | ![output on display error](assets/images/testing/bug_4.png) | Replace with neutral emoji |

## Technologies
- Programming language: Python
- Flake8 for on hand code validation
- CI Python Linter for final code validation
- gspread library for Google Sheets integration
- Google API client installed with google-oauth2 using the Google Cloud Setup

## Credits 

### Resources

- Code Institute's walkthrough project **Love Sandwiches** introduced me to most of the basic functions, module imports and methods.
- As an initial inspiration on how to get started on my project idea I used a [YouTube tutorial](https://www.youtube.com/watch?v=ZBx7oWCJ4aY) that introduced how to use while true loops to build menus.
- To learn about more python string methods, for the input and it's validation, the datetime module, list comprehensions, handling of tuples and more research about built-in functions I have mainly relied on the [W3Schools website](https://www.w3schools.com/python/), sometimes on [Geeksforgeeks](https://www.geeksforgeeks.org/python-datetime-strptime-function/), especially for the datetime module strptime() function, and [Stackoverflow](https://stackoverflow.com/).

### Acknowledgements

I would like to thank my mentor, Rory Patrick Sheridan, for his feedback and guidance.
