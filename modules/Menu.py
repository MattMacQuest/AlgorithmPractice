from modules.menu_options import *
from modules.sorting_algorithms import *

class Menu:
    # Constructor
    def __init__(self, app=None):
        if app:
            self.app = app
        self.options = {}
        self.set_prompt("Please choose an option:")
        self.set_error_text("Invalid menu option.")
    
    # Adds an option to the menu. The options consist of a number, name, and the object 
    # it corresponds to (submenu or function). The last value in each key-value pair
    # denotes whether the given option should trigger an exit from the current menu
    # after it is called    
    def add_option(self, option_number, option_name, option, TriggersExit, *args):
        self.options[option_number] = [option_name, option, TriggersExit, args]
    
    # Sets error text
    def set_error_text(self, error_text):
        self.error_text = error_text
    
    # Sets prompt    
    def set_prompt(self, prompt):
        self.prompt = prompt
    
    # Returns the number of options in this menu
    def size(self):
        return len(self.options)
    
    # Displays the menu's error text
    def disp_error(self):
        system("clear")
        print(self.error_text)
        input("Press enter to continue")
        self.display()
    
    # Prints the menu in its entirety
    def display(self):
        system("clear")
        print(self.prompt)
        for i in range(1, self.size() + 1):
            print(f"{i} - {self.options[i][0]}")
        print()
    
    # Runs the menu
    def run(self):
        user_input = ""
        self.display()
        while True:
            user_input = input("Your selection: ")
            try:
                user_input = int(user_input)
                if user_input <= 0 or user_input > self.size():
                    self.disp_error()
                else:
                    # If the option is a function, call it
                    if callable(self.options[user_input][1]):
                        # This calls the stored function with the optional arguments needed
                        # for several of the function calls. All of these functions should
                        # return to the app object
                        self.options[user_input][1](*self.options[user_input][3])
                        
                        if self.options[user_input][2]:
                            return
                        else:
                            # Otherwise, redisplay the options
                            self.display()
                    # Otherwise it's a submenu, so display it
                    else:
                        self.options[user_input][1].run()
                        self.display()
            except ValueError:
                self.disp_error()
                
def set_menu_hierarchy(app):
    # Create main menu object
    main_menu = Menu(app)
    main_menu.set_prompt("\nSelect an option:")
    
    # Creating the submenus so that we can add them to the main menu
    # Creating the menu for sorting algorithms
    sorting_menu = Menu(app)
    sorting_menu.set_prompt("\nSelect an algorithm to test:")
    sorting_menu.add_option(1, "Bubble Sort", bubble_sort, False, app)
    sorting_menu.add_option(2, "Insertion Sort", insertion_sort, False, app)
    sorting_menu.add_option(3, "Quick Sort", quick_sort, True, app)
    sorting_menu.add_option(4, "Return", Return, True)
    
    # Add searching menu declaration here
    
    # -----------------------------------
    
    # Fill out main menu options
    main_menu.add_option(1, "Sorting Algorithms", sorting_menu, False)
    main_menu.add_option(2, "Generate Unsorted List", generate_list, False, app)
    main_menu.add_option(3, "Exit", Exit, True)
    
    # menu1 = Menu()
    # menu1.set_prompt("\nSelect an option:")
    # menu1.add_option(1, "Option1", Option1, False)
    # menu1.add_option(2, "Return", Return, True)
    
    # menu2 = Menu()
    # menu2.set_prompt("\nWhat would you like help with?")
    # menu2.add_option(1, "My life", MyLife, False)
    # menu2.add_option(2, "Getting help", GettingHelp, False)
    # menu2.add_option(3, "Return", Return, True)
    
    # main_menu.add_option(1, "Enter new values", menu1, False)
    # main_menu.add_option(2, "Help", menu2, False)
    # main_menu.add_option(3, "Exit", Exit, True)
    # main_menu.run()
    
    return main_menu