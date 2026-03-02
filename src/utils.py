import os
from art import text2art
from InquirerPy import inquirer

os.system('color')


def main():
    try:
        result = text2art("BLACKJACK")
        print(result)

        choices = [
            {"name": "[ START GAME ]", "value": "Start"},
            {"name": "[  SETTINGS  ]", "value": "Settings"},
            {"name": "[    EXIT    ]", "value": "Exit"},
        ]

        action = inquirer.select(
            message="Select an action",
            choices=choices,
            pointer=">",
            border=True
        ).execute()

        print(f"Already Selected: {action}")
    except Exception as e:
        print(f"Error de renderizado: {e}")
        action = input("Select (Start/Settings/Exit): ")


if __name__ == "__main__":
    main()
