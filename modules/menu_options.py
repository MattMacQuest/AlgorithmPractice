import sys
from os import system
from modules.sorting_algorithms import *
from modules.generate_list import *
from config import MENU_WIDTH

# Exit function
def Exit():
    system("clear")
    sys.exit(0)

# Returns to previous menu
def Return():
    system("clear")
    return

# Actual menu function to call the function to generate the random list for use in 
# the sorting algorithms
def generate_list(app):
    system("clear")
    line = "=" * MENU_WIDTH
    print(line)
    list_size = None
    
    # Loop is here to validate input
    while not list_size:
        try:
            list_size = int(input("Please enter desired list size: "))
            print(f"Generating unsorted list of size {list_size}...")
            app.unsorted_list = generate_unsorted_list(list_size)
            print("Unsorted list successfully generated")
            return
        
        # I'm not happy with this. I'll need to change how it behaves to make a more elegant
        # input validation loop. 
        except ValueError:
            choice = input("Invalid value entered. Enter 'r' to retry or 'q' to quit")
            if choice == 'r':
                continue
            elif choice == 'q':
                sys.exit(0)
            else:
                sys.exit(1)
            
    