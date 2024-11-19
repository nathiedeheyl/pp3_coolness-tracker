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
    print("Welcome, Friend! 🙂\n\n"
          "You are in the right place\n"
          "if you want to work on lowering your resting heartbeat 🌱\n\n"
          "Track your progress, one day at a time ⏱️\n"
          "towards a healthier heart 🌱\n\n")


def start_menu():
    """
    Display option to show using instructions.
    """
    start_options = ('yes', 'no', 'x')

    while True:
        print("** START MENU **\n\n"
              "yes = See the instructions\n\n"
              "no = Jump to Main Menu\n\n"
              "x = Exit the program\n")

        start_choice = input("Do you need instructions?\n").strip().lower()

        if start_choice in start_options:
            return start_choice

        else:
            print("\nOPTION NOT AVAILABLE!\n\n"
                  "Choose 'yes', 'no' or 'x' to proceed.\n")


def main_menu():
    """
    Display main menu options to enter data or request analysis
    of last week's stats.
    """
    main_options = ('a', 'b', 'x')

    while True:
        print("\n** MAIN MENU **\n\n"
              "What would you like to do next?\n\n"
              "Choose from option 'a' or 'b'\n\n"
              "a - Enter your daily stats\n\n"
              "b - Request an analysis of your health data\n\n"
              "x - Exit program\n")

        main_choice = input("Option:\n").strip().lower()

        if main_choice in main_options:
            return main_choice

        else:
            print("\nOPTION NOT AVAILABLE!\n\n"
                  "Please type in either 'a', 'b', or 'x'\n")


def get_health_stats():
    """
    Get 3 key health metrics from the user, convert all string data to integers
    and validate using try/except to ensure numeric value
    within a specified range, handle ValueError and a loop to prompt user
    to re-enter value if input was incorrect.
    """
    print("You will now be asked for 3 key metrics.\n"
          "Follow the prompts to enter your health data.\n")

    # User data input of resting heart rate
    print("Please enter the lowest heart rate of your last night's sleep.\n"
          "The number should be between 40 - 110.\n")

    while True:
        heartrate_str = input("Enter heartrate here:\n").strip()
        try:
            heartrate = int(heartrate_str)
            if 40 <= heartrate <= 120:
                break
            else:
                print("\nInvalid input! Please enter a number between 40-120\n"
                      "In case of uncertainty, visit your doctor.\n\n")
        except ValueError:
            print("\nInvalid input! Please enter a number.\n\n")

    # User data input of daily minutes of cardio exercise
    print("\nPlease enter the total minutes of cardio exercice of today.\n")

    while True:
        cardio_str = input("Enter exercice minutes:\n").strip()
        try:
            cardio_min = int(cardio_str)
            if 0 <= cardio_min <= 1440:
                break
            else:
                print("\nInvalid input! Please enter the total minutes you\n"
                      "have spent performing cardio exercise today.\n\n")
        except ValueError:
            print("\nInvalid input! Please enter a number.\n\n")

    # User data input of daily minutes of mindful breathing
    print("\nPlease enter today's total minutes of breathing exercise.\n")

    while True:
        breathwork_str = input("Enter mindful breathing minutes:\n").strip()
        try:
            breath_min = int(breathwork_str)
            if 0 <= breath_min <= 1440:
                break
            else:
                print("\nInvalid input! Please enter the total minutes\n"
                      "you have spent doing mindful breathwork today.\n\n")
        except ValueError:
            print("\nInvalid input! Please enter a number.\n\n")

    return heartrate, cardio_min, breath_min


def update_worksheets(data):
    """
    Update spreadsheet, add a new row to each worksheet
    with the corresponding data provided by the user,
    including a timestamp of the date of the data entry.
    """
    heartrate, cardio_min, breath_min = data

    print("\nUpdating worksheets...")

    # Open the corresponding worksheets
    heartrate_worksheet = SHEET.worksheet("heartrate")
    cardio_worksheet = SHEET.worksheet("cardio")
    breathwork_worksheet = SHEET.worksheet("breathwork")

    # Add row to each worksheet with corresponding data
    timestamp = datetime.datetime.now().strftime("%y-%m-%d")
    heartrate_worksheet.append_row([timestamp, heartrate])
    cardio_worksheet.append_row([timestamp, cardio_min])
    breathwork_worksheet.append_row([timestamp, breath_min])

    # Message of success to user
    print("\nHeartrate worksheet updated...\n")
    time.sleep(2)
    print("Cardio worksheet updated...\n")
    time.sleep(2)
    print("Breathwork worksheet updated...\n")
    print("Spreadsheet has been successfully updated.\n")
    time.sleep(2)


def calculate_avr_heartrate():
    """
    Get heartrate worksheet data entries of last 7 days,
    calculate weekly resting heartbeat average and round it;
    display the outcome message to the user.
    """
    today = datetime.datetime.now()

    # Get all values from heartrate (hr) workseet
    hr_sheet = SHEET.worksheet("heartrate").get_all_values()

    # Exclude header from getting all values
    hr_all = hr_sheet[1:]

    # Filter for entries of last 7 days
    hr_week = []
    for row in hr_all:
        tsmp_str = row[0]
        try:
            tsmp = datetime.datetime.strptime(tsmp_str, "%y-%m-%d")
            if (today - tsmp).days <= 7:
                hr_week.append(int(row[1]))
        except ValueError:
            print(f"Error parsing data: {tsmp_str}")

    # Calculate average of last week's entries
    if hr_week:
        hr_avr = sum(hr_week) / len(hr_week)
        hr_rounded = round(hr_avr)
        print(f"Your average resting hear rate was {hr_rounded} bpm")
    else:
        print("Not enough entries yet to calculate weekly average.")

    return hr_rounded


def calculate_sum_cardio():
    """
    Get cardio worksheet data entries of last 7 days,
    calculate the sum and display as total hours and minutes
    to the user with modulo operation.
    """
    today = datetime.datetime.now()

    # Get all values from cardio worksheet
    cardio_sheet = SHEET.worksheet("cardio").get_all_values()

    # Exclude header from all values
    cardio_all = cardio_sheet[1:]

    # Filter for entries of last 7 days
    cardio_week = []
    for row in cardio_all:
        tsmp_str = row[0]
        try:
            if len(row) > 1:
                tsmp = datetime.datetime.strptime(tsmp_str, "%y-%m-%d")
                if (today - tsmp).days <= 7:
                    cardio_week.append(int(row[1]))
        except ValueError:
            print(f"Invalid data on row {row}. Check the spreadsheet.")
            continue

    # Return 0 when less than 7 days of entries
    if not cardio_week:
        print("\nEntry for past 7 days of cardio exercise incomplete.\n\n"
              "Keep tracking your daily exercise mins to enable analysis.\n\n")
        return 0

    # Calculate total time of cardio exercise
    cardio_total = sum(cardio_week)
    cardio_h = cardio_total // 60
    cardio_min = cardio_total % 60
    print(f"\nwith {cardio_h} hours and {cardio_min} minutes of cardio\n")

    return cardio_h, cardio_min


def calculate_sum_breathwork():
    """
    Get breathwork worksheet data entries of last 7 days,
    calculate the sum and display total as a message to the user.
    """
    today = datetime.datetime.now()

    # Get all values from breathwork (breathwork) worksheet
    breathwork_sheet = SHEET.worksheet("breathwork").get_all_values()

    # Exclude header from all values
    breathwork_all = breathwork_sheet[1:]

    # Filter for entries of last 7 days
    breathwork_week = []
    for row in breathwork_all:
        tsmp_str = row[0]
        try:
            if len(row) > 1:
                tsmp = datetime.datetime.strptime(tsmp_str, "%y-%m-%d")
                if (today - tsmp).days <= 7:
                    breathwork_week.append(int(row[1]))
        except ValueError:
            print(f"\nInvalid data on row {row}. Check the spreadsheet.\n\n")
            continue

    # Return 0 when less than 7 days of entries
    if not breathwork_week:
        print("\nEntry for past 7 days of breathing exercise incomplete.\n\n"
              "Keep tracking your daily mindfulnes mins to enable analysis.\n")
        return 0

    # Calculate total time of breathwork exercise
    breathwork_mins = sum(breathwork_week)
    print(f"and {breathwork_mins} minutes of relaxing, mindful breathwork.\n")

    return breathwork_mins


def main():
    """
    Run all program functions
    """
    display_welcome_message()

    # Run Start Menu:
    start_choice = start_menu()

    # Start Menu option handling
    if start_choice == 'yes':
        print("\n--- How to use this program ---\n"
              "\nWe recommend using a smart wearable or similar.\n"
              "\nAt the end of each day, enter your daily stats: \n"
              "    • Lowest heart rate during your last sleep\n"
              "    • Total minutes of cardio exercises of that day\n"
              "    • Total minutes of intentional breathwork in that day\n"
              "\nThe program will let you choose between: Enter your data\n"
              "or request an analysis of your current health state.\n"
              "\nYou can always return to the main menu.\n"
              "\nRestart the program to see the instructions again.\n")

        # Proceed to main menu confirmation
        print("Proceed to MAIN MENU?")
        input("Press ENTER\n")

    elif start_choice == 'no':
        print("\nRedirecting to Main Menu...")

    elif start_choice == 'x':
        print("\nBye! See you soon 🙂")
        exit()

    # Run Main Menu Loop
    while True:
        main_choice = main_menu()

        # Main Menu option handling
        if main_choice == 'a':
            heartrate, cardio_min, breath_min = get_health_stats()
            update_worksheets((heartrate, cardio_min, breath_min))
            print("\nReturning to Main Menu...\n")
            time.sleep(2)

        elif main_choice == 'b':
            print("\nCalculating averages... analyzing...\n")
            time.sleep(2)
            hr_rounded = calculate_avr_heartrate()
            cardio_h, cardio_min = calculate_sum_cardio()
            breathwork_mins = calculate_sum_breathwork()
            print("\nGood job! Keep tracking your stats for more insight.\n\n"
                  "\nGo back to Main Menu?\n")
            input("Press ENTER\n")

        elif main_choice == 'x':
            print("\nBye! See you soon 🙂\n")
            exit()


main()
