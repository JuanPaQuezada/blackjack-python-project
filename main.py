# +----------------------------------------------------------------------------+
# | Authors.......: Juan Pablo Quezada Jimenez <qjuanpablo21@gmail.com>
# | First release: February 11th, 2026
# | Last update..: February 11th, 2026
# | WhatIs.......: Blackjack Game - Main
# +----------------------------------------------------------------------------++
# ------------------------- Instructions -----------------------
# TODO:

# ------------ Resources / Documentation involved -------------
# The Translator in Your Computer: https://cpu.land/the-translator-in-your-computer

# ------------------------- Libraries -------------------------
from src.utils import get_center_padding,clear_screen
import os
from art import text2art
from InquirerPy import inquirer
# ------------------------- Functions -------------------------

os.system('color')

class Pantalla:
    def __init__(self, title, options):
        self.title = title
        self.options = options
    def render(self):
        clear_screen()
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



# ------------------------- Variables -------------------------

# --------------------------- Code ----------------------------
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
