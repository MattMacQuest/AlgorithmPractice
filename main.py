from modules import Menu
from modules import Application
# from modules.ConfigManager import *

def main():
    print("Welcome to the sorting algorithm efficiency tester!")
    
    app = Application.Application()
    main_menu = Menu.set_menu_hierarchy(app)
    main_menu.run()

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