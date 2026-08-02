"""
==========================================================
AI Powered Cybersecurity Threat Detection System
----------------------------------------------------------
Project Launcher

Description:
    Entry point of the application.
==========================================================
"""

import os


def clear_screen():

    os.system(
        "cls" if os.name == "nt" else "clear"
    )


def menu():

    while True:

        clear_screen()

        print("=" * 60)
        print(" AI Powered Cybersecurity Threat Detection System")
        print("=" * 60)

        print("\n1. Train Model")
        print("2. Detect Threat")
        print("3. Exit")

        choice = input("\nEnter your choice : ").strip()

        if choice == "1":

            os.system("python train.py")

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "2":

            os.system("python detect.py")

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "3":

            print("\nThank You.\n")
            break

        else:

            print("\nInvalid Choice.")

            input(
                "\nPress Enter to continue..."
            )


if __name__ == "__main__":

    menu()