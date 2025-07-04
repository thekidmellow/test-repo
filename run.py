import os
import re


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def main():
    """
    Displays a menu and handles user input.
    """

    print("Hotel Management System\n")
    print("1. Add Guest")
    print("2. View All Guests")
    print("3. Search Guest by Email")
    print("4. Update Guest")
    print("5. Delete Guest")
    print("6. Exit\n")


# Start the program
clear()
main()
