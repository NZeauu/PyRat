from Settings.Config import *
from Settings.Utils import *

import subprocess
import sys
import time


def ask_choice():
    choice = input(f"{colorama.Fore.RED}>>{colorama.Fore.RESET}")
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
            start_tool(categories[choice], f"{choices[choice]}.py")
        elif "0" + choice in choices:
            start_tool(categories["0" + choice], f"{choices['0' + choice]}.py")
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

        while not r:
            clear()
            print(banner)
            print(main_menu)
            print(f"{colorama.Fore.RED}Invalid choice. Please try again.{colorama.Fore.RESET}")
            choice = ask_choice()
            r = select_tool(choice)


    except Exception as e:
        print("An error occurred during installation. Please try again.")
        print("If the problem persists, please contact the developer.")
        print(f"Error: {e}")
        break