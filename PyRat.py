from Settings.Config import *
from Settings.Utils import *

def ask_choice() -> str:
    """Ask the user for a choice

    Returns:
        str: The user's choice
    """
    choice = input(f"{bright}{red}>> {reset_all}")
    return choice

def select_tool(choice: str) -> bool:
    """Select a tool based on the user's choice

    Args:
        choice (str): The user's choice

    Returns:
        bool: True if the tool was found, False otherwise
    """
    # Exit program
    if choice == "Q" or choice == "q":
        exit_program()

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
        # print(main_menu)
        print_menu()


        # Check if a new version of the tool is available
        check_for_update()


        choice = ask_choice()

        r = select_tool(choice)

        # break

        while not r:
            clear()
            print(banner)
            # print(main_menu)
            print_menu()
            print_error("Invalid choice. Please try again.")
            choice = ask_choice()
            r = select_tool(choice)


    except Exception as e:
        print_error(f"An error occurred: {e}")
        wait_user()
        exit()
    except KeyboardInterrupt:
        exit_program()