from modules.generate_list import *
from modules.Menu import *
from modules.Application import *
# from modules.timekeeper import *
# from time import perf_counter
# from modules.ConfigManager import *
# from os import system
# from config import MAIN_MENU_OPTIONS, MENU_WIDTH
# from menu_test import *

# app = Application()

def main():
    print("Welcome to the sorting algorithm efficiency tester!")
    
    # main_menu_options = dict(enumerate(MAIN_MENU_OPTIONS, start=1))
    # unsorted_list = []
    app = Application()
    main_menu = set_menu_hierarchy(app)
    main_menu.run()
    
    # main_menu = Menu()
    # main_menu.set_prompt("\nSelect an option:")
    
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