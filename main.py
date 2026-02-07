from modules.generate_list import *
from modules.menu import *
# from modules.timekeeper import *
# from time import perf_counter
from modules.ConfigManager import *
from os import system
from config import MAIN_MENU_OPTIONS, MENU_WIDTH

def main():
    print("Welcome to the sorting algorithm efficiency tester!")
    
    main_menu_options = dict(enumerate(MAIN_MENU_OPTIONS, start=1))
    unsorted_list = []
    
    # print_menu("Main Menu", menu_options)
    while True:
        print_menu("Main Menu", main_menu_options)
        selection = input("Select an option: ")
        
        # I hate this. As written will result in nested match statements and spaghetti.
        # I need to migrate this elsewhere and change how I handle it. Might be time 
        # to use an external menu library. Main challenge: data persistence (The unsorted list
        # must be generated on demand, of a specified size, and be usable across menus) preferably
        # without the use of globals. An Application class could fix this as the scope of this
        # is growing out of control and getting far more general
        match main_menu_options[int(selection)]:
            case "Quit":
                system('clear')
                return 0
            case "Sorting Algorithms":
                print_menu("Sorting Algorithms")
                input("Press enter to continue")
                continue
            case "Searching Algorithms":
                print_menu("Searching Algorithms")
                input("Press enter to continue")
                continue
            case "Generate Unsorted List":
                system('clear')
                line = "=" * MENU_WIDTH
                print(line)
                try:
                    list_size = int(input("Enter list size: "))
                    print(f"Generating random unsorted list of size {list_size}...")
                    unsorted_list = generate_unsorted_list(list_size)
                    print("Unsorted list successfully generated")
                    input("Press enter to continue...")
                    continue
                    
                except ValueError as v:
                    print(v)
                    input("Press enter to continue...")
                    continue
            case "Settings":
                continue
            case _:
                continue

        # if main_menu_options[int(selection)] == "Quit":
        #     system('clear')
        #     break
    
    # random_list = generate_unsorted_list(300000000)

if __name__ == "__main__":
    # Commented out as an example of how the ConfigManager will be used in the future
    # config_mgr = ConfigManager()
    
    # dev_config = {
    #     'database': {
    #         'host': 'localhost',
    #         'port': 5432,
    #         'name': 'dev_db'
    #     },
    #     'api': {
    #         'base_url': 'http://localhost:8000',
    #         'timeout': 30
    #     }
    # }
    
    # config_mgr.save_config('development', dev_config)
    
    # config_mgr.load_config('development')
    # print(f"Database host: {config_mgr.get('database.host')}")
    # print(f"API timeout: {config_mgr.get('api.timeout')}")
    
    main()