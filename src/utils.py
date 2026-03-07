import os
import shutil
from art import text2art
from InquirerPy import inquirer

os.system('color')


def get_center_padding(text):
    terminal_width = shutil.get_terminal_size().columns
    max_line_width = max(len(line) for line in text.splitlines())
    padding = (terminal_width - max_line_width) // 2
    return max(0, padding)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
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
