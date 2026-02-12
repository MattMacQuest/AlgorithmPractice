import sys
from os import system
from modules import sorting_algorithms, timekeeper
import modules.generate_list as generate_list
from time import perf_counter
from config import MENU_WIDTH, LIST_PREVIEW_LENGTH

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
def do_generate_list(app):
    system("clear")
    line = "=" * MENU_WIDTH
    # print(line)
    list_size = None
    
    # Loop is here to validate input
    while not list_size:
        try:
            list_size = int(input("Please enter desired list size: "))
            print(f"Generating unsorted list of size {list_size}...")
            # app.current_lists["Unsorted"] = do_generate_list.generate_unsorted_list(list_size)
            app.set_unsorted(generate_list.generate_unsorted_list(list_size))
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
            
# def display_list(app, key):
#     system("clear")
#     line = "=" * MENU_WIDTH
#     print(line, "\n")
#     if len(app.current_lists[key]) <= LIST_PREVIEW_LENGTH:
#         print(app.current_lists[key], "\n")
#     else:
#         print("[", end="")
#         for i in range(LIST_PREVIEW_LENGTH):
#             if i < LIST_PREVIEW_LENGTH - 1:
#                 print(app.current_lists[key][i], end=", ")
#             else:
#                 print(app.current_lists[key][i], end=", ...]\n\n")
#     print(line)
#     print()
#     input("Press enter to continue")
    
# Perhaps modify this to work better with the past entries. Could add another optional arg to indicate
# whether it's a current or past list, and if it's a past list, add an extra loop to go through the 2D
# list instead
def display_list(dict, key, past_list=False):
    system("clear")
    line = "=" * MENU_WIDTH
    print(line, "\n")
    if not past_list:
        if len(dict[key]) <= LIST_PREVIEW_LENGTH:
            print(f"List size: {len(dict[key])}")
            print(dict[key], "\n")
        else:
            print(f"List size: {len(dict[key])}")
            print("[", end="")
            for i in range(LIST_PREVIEW_LENGTH):
                if i < LIST_PREVIEW_LENGTH - 1:
                    print(dict[key][i], end=", ")
                else:
                    print(dict[key][i], end=", ...]\n\n")
    else:
        counter = 1
        for prev_list in dict[key]:
            print(f"{counter}.", end=" ")
            if len(prev_list) <= LIST_PREVIEW_LENGTH:
                print(prev_list, "\n")
                # print(prev_list)
            else:
                print("[", end="")
                for i in range(LIST_PREVIEW_LENGTH):
                    if i < LIST_PREVIEW_LENGTH - 1:
                        print(prev_list[i], end=", ")
                    else:
                        print(prev_list[i], end=", ...]\n\n")
            counter += 1
            
    print(line)
    print()
    input("Press enter to continue")
    
def do_quick_sort(app):
    system("clear")
    timekeeper.log("Starting quick sort")
    
    print(f"Sorting list of size {len(app.current_lists["Unsorted"])}:")
    
    if len(app.current_lists["Unsorted"]) <= LIST_PREVIEW_LENGTH:
        print(app.current_lists["Unsorted"], "\n")
    else:
        print("[", end="")
        for i in range(LIST_PREVIEW_LENGTH):
            if i < LIST_PREVIEW_LENGTH - 1:
                print(app.current_lists["Unsorted"][i], end=", ")
            else:
                print(app.current_lists["Unsorted"][i], end=", ...]\n\n")
    
    start = perf_counter()
    
    high = len(app.current_lists["Unsorted"]) - 1
    app.set_sorted(sorting_algorithms.quick_sort(app.current_lists["Unsorted"], 0, high))
    
    end = perf_counter()
    
    timekeeper.log("Quick sort complete", end - start)
    
    print(f"Sorted list of size {len(app.current_lists["Sorted"])}:")
    if len(app.current_lists["Sorted"]) <= LIST_PREVIEW_LENGTH:
        print(app.current_lists["Sorted"], "\n")
    else:
        print("[", end="")
        for i in range(LIST_PREVIEW_LENGTH):
            if i < LIST_PREVIEW_LENGTH - 1:
                print(app.current_lists["Sorted"][i], end=", ")
            else:
                print(app.current_lists["Sorted"][i], end=", ...]\n\n")
                
    input("Press enter to continue")

def do_insertion_sort(app):
    system("clear")
    timekeeper.log("Starting insertion sort")
    
    print(f"Sorting list of size {len(app.current_lists["Unsorted"])}:")
    
    if len(app.current_lists["Unsorted"]) <= LIST_PREVIEW_LENGTH:
        print(app.current_lists["Unsorted"], "\n")
    else:
        print("[", end="")
        for i in range(LIST_PREVIEW_LENGTH):
            if i < LIST_PREVIEW_LENGTH - 1:
                print(app.current_lists["Unsorted"][i], end=", ")
            else:
                print(app.current_lists["Unsorted"][i], end=", ...]\n\n")
    
    start = perf_counter()
    
    app.set_sorted(sorting_algorithms.quick_sort(app.current_lists["Unsorted"]))
    
    end = perf_counter()
    
    timekeeper.log("Insertion sort complete", end - start)
    
    print(f"Sorted list of size {len(app.current_lists["Sorted"])}:")
    if len(app.current_lists["Sorted"]) <= LIST_PREVIEW_LENGTH:
        print(app.current_lists["Sorted"], "\n")
    else:
        print("[", end="")
        for i in range(LIST_PREVIEW_LENGTH):
            if i < LIST_PREVIEW_LENGTH - 1:
                print(app.current_lists["Sorted"][i], end=", ")
            else:
                print(app.current_lists["Sorted"][i], end=", ...]\n\n")
                
    input("Press enter to continue")

def do_bubble_sort(app):
    system("clear")
    timekeeper.log("Starting bubble sort")
    
    print(f"Sorting list of size {len(app.current_lists["Unsorted"])}:")
    
    # This prints the first LIST_PREVIEW_LENGTH items in a list in readable, list-style format
    # I could roll this into a generic print function to save on repeated code as it shows up
    # multiple times as is. I even have a generic display_list function up there ^^^
    if len(app.current_lists["Unsorted"]) <= LIST_PREVIEW_LENGTH:
        print(app.current_lists["Unsorted"], "\n")
    else:
        print("[", end="")
        for i in range(LIST_PREVIEW_LENGTH):
            if i < LIST_PREVIEW_LENGTH - 1:
                print(app.current_lists["Unsorted"][i], end=", ")
            else:
                print(app.current_lists["Unsorted"][i], end=", ...]\n\n")
    
    # Roll this into some timekeeper function to clean it up maybe?
    start = perf_counter()
    sorting_algorithms.bubble_sort(app)
    end = perf_counter()
    
    timekeeper.log("Bubble sort complete", end - start)
    
    print(f"Sorted list of size {len(app.current_lists["Sorted"])}:")
    if len(app.current_lists["Sorted"]) <= LIST_PREVIEW_LENGTH:
        print(app.current_lists["Sorted"], "\n")
    else:
        print("[", end="")
        for i in range(LIST_PREVIEW_LENGTH):
            if i < LIST_PREVIEW_LENGTH - 1:
                print(app.current_lists["Sorted"][i], end=", ")
            else:
                print(app.current_lists["Sorted"][i], end=", ...]\n\n")
                
    input("Press enter to continue")