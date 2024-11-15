import gspread
from google.oauth2.service_account import Credentials
# import time

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
    upon start of the program explaining it's purpose and how to use it.
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


display_welcome_message()


def start_menu():
    start_options = ('yes', 'no', 'x')

    while True:
        print()
        print("** MENU **")
        print()
        print("yes = See the instructions")
        print("no = Jump to the next step")
        print("x = Exit the program")

        start_choice = input("\nDo you need instructions? ").strip().lower()

        if start_choice in start_options:
            # break out of the loop by using the keyword break
            # or returning a value?
            return start_choice

        else:
            print()
            print("OPTION NOT AVAILABLE!")
            print("Choose 'yes', 'no' or 'x' to proceed.")


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
    print("The programm will let you choose between: Enter your data")
    print("Or request an analysis of your current health state.")
    print()
    print("You can always return to the main menu.")
    print()
    print("Restart the program to see the instructions again")
    # Give option to call main menu function

# elif start_choice == 'no':
    # Redirect: Clicked no, wait
    # Call main menu function

elif start_choice == 'x':
    print()
    print("Bye! See you soon 🙂")
    exit()
