from Settings.Config import *
from Settings.Utils import *

try:
    import sys
    import time
except ImportError:
    module_error()

def ask_choice():
    choice = input(f"{red}>>{reset}")
    return choice

def select_tool(choice):
    
    # Exit program
    if choice == "Q" or choice == "q":
        clear()
        print(banner)
        print(f"""{white}Exiting PyRat...{reset}""")
        time.sleep(2)
        clear()
        sys.exit()
    else:
        if choice in choices:
            start_tool(categories[choice], f"{choices[choice]}")
        elif "0" + choice in choices:
            start_tool(categories["0" + choice], f"{choices['0' + choice]}")
        else:
            return False
        
        return True
    

while True:
    try:
        clear()

        print(banner)
        print(main_menu)

        choice = ask_choice()

        r = select_tool(choice)

        # break

        while not r:
            clear()
            print(banner)
            print(main_menu)
            print(f"{red}Invalid choice. Please try again.{reset}")
            choice = ask_choice()
            r = select_tool(choice)


    except Exception as e:
        print("An error occurred during installation. Please try again.")
        print("If the problem persists, please contact the developer.")
        print(f"Error: {e}")
        break