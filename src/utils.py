import os
import shutil
from random import choices

from art import text2art
from InquirerPy import inquirer

os.system('color')

class Pantalla:
    def __init__(self, title, options):
        self.title = title
        self.options = options
    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            result = text2art(self.title)
            espacios = get_center_padding(result)
            for linea in result.splitlines():
                print(" "*espacios + linea)
            print("\n")

            options_text = "\n".join(c["name"] for c in self.options)
            space = get_center_padding(options_text)
            space = max(0, space - 2)
            center_pointer = (" " * space) + "> "

            action = inquirer.select(
                message="Select an action",
                choices=self.options,
                pointer=center_pointer,
                border=True
            ).execute()

            print(f"Already Selected: {action}")
            return action
        except Exception as e:
            print(f"Error de renderizado: {e}")
            action = input("Select (Start/Settings/Exit): ")


def get_center_padding(text):
    terminal_width = shutil.get_terminal_size().columns
    max_line_width = max(len(line) for line in text.splitlines())
    padding = (terminal_width - max_line_width) // 2
    return max(0, padding)

def main():
    choices = [
        {"name": "[ START GAME ]", "value": "Start"},
        {"name": "[  SETTINGS  ]", "value": "Settings"},
        {"name": "[    EXIT    ]", "value": "Exit"},
    ]

    pantallaPrincipal = Pantalla("BLACKJACK",choices)
    seccion = pantallaPrincipal.render()

if __name__ == "__main__":
    main()
