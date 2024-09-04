import sys
import os

def print_pretty(content, width=30, separator='-'):
    print(separator * width)
    print(f"{content:^{width}}")
    print(separator * width)

    
try:

    if sys.prefix == sys.base_prefix:
        raise Exception("""
                        Please run the installation script in a virtual environment.
                        To create a virtual environment, run the following commands:
                        - python -m venv path/to/venv
                        - source venv/bin/activate (Linux) or venv\Scripts\\activate (Windows)
                        """)

    from Settings.Config import *   

    print_pretty(f"{tool_name} Version: {tool_version}")

    print(f"\nThanks for downloading {tool_name}. Installation is in progress. Please wait...\n")

    if sys.platform.startswith('win'):
        os.system('pip install -r requirements.txt')

    elif sys.platform.startswith('linux'):
        os.system('pip3 install -r requirements.txt')



except Exception as e:
    print("An error occurred during installation. Please try again.")
    print("If the problem persists, please contact the developer.")
    print(f"Error: {e}")