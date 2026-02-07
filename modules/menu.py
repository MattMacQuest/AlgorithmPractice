import yaml
import sys
from os import system
from config import MENU_WIDTH

# Print function for the various menus
def print_menu(title, menu_options={}):
    system('clear')
    title = title.center(len(title) + 2, " ")
    line = title.center(MENU_WIDTH, "=")
    border = "=" * MENU_WIDTH
    print(line)
    for key in menu_options:
        print(key, menu_options[key])
    print(border)
    
    