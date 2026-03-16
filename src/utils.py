import os
import shutil

def get_center_padding(text):
    terminal_width = shutil.get_terminal_size().columns
    max_line_width = max(len(line) for line in text.splitlines())
    padding = (terminal_width - max_line_width) // 2
    return max(0, padding)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
