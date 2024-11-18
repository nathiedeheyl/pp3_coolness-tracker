import gspread
from google.oauth2.service_account import Credentials
import datetime
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('coolness_tracker')


def display_welcome_message():
    """
    Displays a friendly and encouraging welcome message
    upon start of the program.
    """
    print()
    print("Welcome, Friend! 🙂")
    print()
    print("You are in the right place")
    print("if you want to work on lowering your resting heartbeat 🌱")
    print()
    print("Track your progress, one day at a time ⏱️")
    print("towards a healthier heart 🌱")
    print()


def start_menu():
    """
    Display option to show using instructions.
    """
    start_options = ('yes', 'no', 'x')

    while True:
        print()
        print("** START MENU **")
        print()
        print("yes = See the instructions")
        print("no = Jump to Main Menu")
        print("x = Exit the program")

        start_choice = input("\nDo you need instructions?\n").strip().lower()

        if start_choice in start_options:
            return start_choice

        else:
            print()
            print("OPTION NOT AVAILABLE!")
            print("Choose 'yes', 'no' or 'x' to proceed.")


def main_menu():
    """
    Display main menu options to enter data or request analysis.
    """
    main_options = ('a', 'b', 'x')

    while True:
        print()
        print("** MAIN MENU **")
        print()
        print("What would you like to do next?")
        print("Choose from option 'a' or 'b'")
        print()
        print("a - Enter your daily stats")
        print()
        print("b - Request an analysis of your health data")
        print()
        print("x - Exit program")
        print()

        main_choice = input("\nOption:\n").strip().lower()

        if main_choice in main_options:
            return main_choice

        else:
            print()
            print("OPTION NOT AVAILABLE!")
            print("Please type in either 'a', 'b', or 'x'")


def get_health_stats():
    """
    Get 3 key health metrics from the user, convert all string data to integers
    and validate using try/except to ensure numeric value
    within a specified range, handle ValueError and a loop to prompt user
    to re-enter value if input was incorrect.
    """
    print()
    print("You will now be asked for 3 key metrics.")
    print("Follow the prompts one after another to enter your health data.")
    print()
    print("Please enter the lowest heart rate during your last night's sleep.")
    print("The number should be between 40-110.")
    print()

    while True:
        heartrate_str = input("Enter heartrate here:\n").strip()
        try:
            heartrate = int(heartrate_str)
            if 40 <= heartrate <= 120:
                break
            else:
                print()
                print("Invalid input! Please enter a number between 40 - 120.")
                print("In case of uncertainty, visit your doctor.")
                print()
        except ValueError:
            print()
            print("Invalid input! Please enter a number.")
            print()

    print()
    print("Please enter the total minutes of cardio exercice of today.")
    print()

    while True:
        cardio_str = input("Enter exercice minutes:\n").strip()
        try:
            cardio_min = int(cardio_str)
            if 0 <= cardio_min <= 1440:
                break
            else:
                print()
                print("Invalid input! Please enter the total minutes you")
                print("have spent performing cardiovascular exercise today.")
                print()
        except ValueError:
            print()
            print("Invalid input! Please enter a number.")
            print()

    print()
    print("Please enter the total minutes of minful braethwork of today.")
    print()

    while True:
        breathwork_str = input("Enter mindful breathing minutes:\n").strip()
        try:
            breath_min = int(breathwork_str)
            if 0 <= breath_min <= 1440:
                break
            else:
                print()
                print("Invalid input! Please enter the total minutes")
                print("you have spent doing mindful breathwork today.")
                print()
        except ValueError:
            print()
            print("Invalid input! Please enter a number.")
            print()

    return heartrate, cardio_min, breath_min


def update_worksheets(data):
    """
    Update spreadsheet, add a new row to each worksheet
    with the corresponding data provided by the user,
    including a timestamp of the date of the data entry.
    """
    heartrate, cardio_min, breath_min = data

    print("Updating worksheets...")

    # Open the corresponding worksheets
    heartrate_worksheet = SHEET.worksheet("heartrate")
    cardio_worksheet = SHEET.worksheet("cardio")
    breathwork_worksheet = SHEET.worksheet("breathwork")

    # Add row to each worksheet with corresponding data
    timestamp = datetime.datetime.now().strftime("%y-%m-%d")
    heartrate_worksheet.append_row([timestamp, heartrate])
    cardio_worksheet.append_row([timestamp, cardio_min])
    breathwork_worksheet.append_row([timestamp, breath_min])

    print()
    print("Heartrate worksheet updated...")
    print()
    time.sleep(2)
    print("Cardio worksheet updated...")
    print()
    time.sleep(2)
    print("Breathwork worksheet updated...")
    print()
    print("Spreadsheet has been successfully updated.")
    time.sleep(2)


def calculate_weekly_stats():
    """
    Get worksheet data entries of last 7 days,
    calculate weekly resting heartbeat average (rounded),
    total hours + minutes of cardio and minutes of breathwork per week
    and display the outcome as message to the user.
    """
    print("\nCalculating averages... analyzing...\n")
    time.sleep(2)

    today = datetime.datetime.now()

    # Get all values from heartrate (hr) workseet
    hr_sheet = SHEET.worksheet("heartrate").get_all_values()

    # Exclude header from getting all values
    hr_all = hr_sheet[1:]

    print(hr_all)
    print()

    # Filter for entries of last 7 days
    hr_week = []
    for row in hr_all:
        tsmp_str = row[0]
        try:
            tsmp = datetime.datetime.strptime(tsmp_str, "%y-%m-%d")
            if (today - tsmp).days <= 7:
                hr_week.append(int(row[1]))
        except ValueError:
            print(f"Invalid time format: {tsmp_str}")

    print(hr_week)

    # Calculate average of last week's entries
    if hr_week:
        hr_avr = sum(hr_week) / len(hr_week)
        hr_avr_rd = round(hr_avr)
        print(f"Your average resting hear rate was {hr_avr_rd} bpm")
    else:
        print("Not enough entries yet to calculate weekly average.")

    return hr_avr_rd


def main():
    """
    Run all program functions
    """
    display_welcome_message()

    # Run Start Menu:

    start_choice = start_menu()

    if start_choice == 'yes':
        print()
        print("--- How to use this program ---")
        print()
        print("We recommend using a smart wearable or similar.")
        print()
        print("At the end of each day, enter your daily stats: ")
        print("    • Lowest heart rate during your last sleep")
        print("    • Total minutes of cardio exercises of that day")
        print("    • Total minutes of intentional breathwork in that day")
        print()
        print("The program will let you choose between: Enter your data")
        print("Or request an analysis of your current health state.")
        print()
        print("You can always return to the main menu.")
        print()
        print("Restart the program to see the instructions again.")

        # Proceed to main menu confirmation
        print("\nProceed to main?")
        input("Press ENTER\n")

    elif start_choice == 'no':
        print("Redirecting to Main Menu...")

    elif start_choice == 'x':
        print()
        print("Bye! See you soon 🙂")
        exit()

    # Run Main Menu Loop

    while True:
        main_choice = main_menu()

        if main_choice == 'a':
            heartrate, cardio_min, breath_min = get_health_stats()
            update_worksheets((heartrate, cardio_min, breath_min))
            print("\nReturning to Main Menu...\n")
            time.sleep(2)

        elif main_choice == 'b':
            hr_avr_rd = calculate_weekly_stats()
            print("\nGo back to Main Menu?")
            input("Press ENTER\n")

        elif main_choice == 'x':
            print()
            print("Bye! See you soon 🙂")
            exit()


main()
