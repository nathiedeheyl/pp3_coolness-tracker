import gspread
from google.oauth2.service_account import Credentials
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

        start_choice = input("\nDo you need instructions? ").strip().lower()

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

        main_choice = input("\nOption: ").strip().lower()

        if main_choice in main_options:
            return main_choice

        else:
            print()
            print("OPTION NOT AVAILABLE!")
            print("Please type in either 'a', 'b' 'x'")


def main():
    """
    Run all program function
    """
    display_welcome_message()

    # Run Start Menu:
    while True:
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
            print("Restart the program to see the instructions again.")

            # Proceed to main menu confirmation
            while True:
                print("\nProceed to main?")
                proceed_main = input("Press 'y' and ENTER:\n").strip().lower()
                if proceed_main == 'y':
                    main_menu()
                    break
                else:
                    print("Invalid input. Please press 'y' to proceed.")

        elif start_choice == 'no':
            print("Redirecting to Main Menu...")
            time.sleep(3)
            main_menu()

        elif start_choice == 'x':
            print()
            print("Bye! See you soon 🙂")
            exit()

    # Run Main Menu:
    while True:
        main_choice = main_menu()

        if main_choice == 'a':
            print()
            time.sleep(3)
            print("You chose 'a'")

        elif main_choice == 'b':
            print()
            time.sleep(3)
            print("You chose 'b'")

        elif main_choice == 'x':
            print()
            print("Bye! See you soon 🙂")
            exit()


main()
