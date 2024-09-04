import os
import sys
import subprocess

tool_path = os.path.dirname(os.path.abspath(__file__)).split("Settings")[0].strip()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def start_tool(category, tool_name):
    if sys.platform.startswith('win'):
        file = "python", os.path.join(tool_path, "Tools", category, tool_name)
        subprocess.run(file)
    elif sys.platform.startswith('linux'):
        file = "python3", os.path.join(tool_path, "Tools", category, tool_name)
        subprocess.run(file)