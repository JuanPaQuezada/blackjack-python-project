import os
import shutil

SYMBOLS = {
    'Corazones': '♥',
    'Diamantes': '♦',
    'Treboles': '♣',
    'Picas': '♠'
}

class Card:
    def __init__(self, simbol, suit, rank):
        self.simbol = simbol
        self.suit = suit
        self.rank = rank

    #@Jon agregar plantilla de cartas de forma dinamica 1 sola plantilla(1 sola carta)
    def __str__(self):
        print_cards(suit, rank)



def get_center_padding(text):
    terminal_width = shutil.get_terminal_size().columns
    max_line_width = max(len(line) for line in text.splitlines())
    padding = (terminal_width - max_line_width) // 2
    return max(0, padding)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_template(suit, rank):
    s = SYMBOLS.get(suit,suit)
    r=str(rank).ljust(2)

    template = [
        "┌─────────┐",
        f"│ {r}      │",
        "│         │",
        f"│    {s}    │",
        "│         │",
        f"│      {r} │",
        "└─────────┘"
    ]

    return template


def print_cards(cards_list):
    lines = ["","","","","","",""]
    for card in cards_list:
        template = generate_template(card.suit, card.rank)
        for i in range(7):
            lines[i] += template[i] + " "

    for level in lines:
        print(level)