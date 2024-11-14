import gspread
from google.oauth2.service_account import Credentials

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
    print("\nWelcome, Friend! 🙂\n")
    print("You are in the right place")
    print("if you want to work on lowering your resting heartbeat 🌱")
    print("\nTrack your progress, one day at a time ⏱️")
    print("towards a healthier heart 🌱\n")


display_welcome_message()
