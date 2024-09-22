import os
import sys
from .Config import *

try:
    import subprocess
    import colorama
    import re
    import time
    import requests
    from terminaltables import SingleTable

except ImportError:
    print(f"An error occurred while trying to import a module.")
    print(f"Please make sure you have all the necessary modules installed using requirements.txt or Setup.py.")
    print(f"If the problem persists, please contact the developer.")
    input(f"Press Enter to continue...")
    sys.exit()


tool_path = os.path.dirname(os.path.abspath(__file__)).split("Settings")[0].strip()


def clear():
    """Clear the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def start_tool(category: str, tool_name: str):
    """Start a tool from the selected category.

    Args:
        category (str): The category of the tool.
        tool_name (str): The name of the tool.
    """

    clear()
    if tool_name == "soon":
        print("Soon available...")
        input("Press Enter to continue...")
        return

    if sys.platform.startswith('win'):
        file = f"python -m Settings.Tools.{category}.{tool_name}"
        subprocess.run(file, shell=True)
    elif sys.platform.startswith('linux'):
        file = f"python3 -m Settings.Tools.{category}.{tool_name}"
        subprocess.run(file, shell=True)


def module_error():
    """Print an error message when a module is not found.
    """
    print(f"An error occurred while trying to import a module.")
    print(f"Please make sure you have all the necessary modules installed using requirements.txt or Setup.py.")
    print(f"If the problem persists, please contact the developer.")
    input(f"Press Enter to continue...")
    exit()

def validate_ip(ip: str) -> bool:
    """Validate an IP address.

    Args:
        ip (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """

    if re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip):
        return True

    print_error("Invalid IP address!")
    return False

def validate_email(email: str) -> bool:
    """Validate an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """

    if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return True

    print_error("Invalid email address!")
    return False

def exit_program():
    """Exit the program.
    """
    clear()
    print(banner)
    print_message("Exiting PyRat...")
    time.sleep(2)
    clear()
    sys.exit()

def print_message(message: str):
    """Print a message to the console.

    Args:
        message (str): The message to print.
    """
    print(f"{message_start} {message}{reset}")

def print_error(message: str):
    """Print an error message to the console.

    Args:
        message (str): The error message to print.
    """
    print(f"{error_start} {message}{reset_all}")

def wait_user():
    """Wait for the user to press Enter.
    """
    input(f"{message_start} Press Enter to continue...{reset}")


def print_menu():
    """Print the main menu to the console.
    """
    table = SingleTable(table_data)
    table.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center', 4: 'center'}
    print(f"{red}")
    print(table.table)
    print(f"{green}[Q]-Exit{reset}\n")


def check_for_update():
    """Check for a new version of the tool on GitHub.
    """
    url = "https://raw.githubusercontent.com/NZeauu/PyRat/main/Settings/Config.py"

    print_message("Checking for updates...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        match = re.search(r'tool_version\s*=\s*[\'"]([^\'"]+)[\'"]', content)

        if match:
            remote_version = match.group(1)

            if remote_version != tool_version:
                print(f"{warning_start} A new version of PyRat is available! Please update to version {remote_version}")
                print(f"{warning_start} Visit {github_url} to download the latest version.")

            else:
                print_message("PyRat is up to date.")
        
    except requests.exceptions.RequestException as e:
        print_error(f"An error occurred while trying to check for updates: {e}")


# ======================================================================================================================
# |                                                     APP MENUS                                                      |
# ======================================================================================================================

red = colorama.Fore.RED
green = colorama.Fore.GREEN
white = colorama.Fore.WHITE
yellow = colorama.Fore.YELLOW
blue = colorama.Fore.BLUE
reset = colorama.Fore.RESET
bright = colorama.Style.BRIGHT
reset_all = colorama.Style.RESET_ALL

error_start = f"{bright}{red}[!]{reset_all}{white}"
warning_start = f"{bright}{yellow}[!]{reset_all}{white}"
message_start = f"{bright}{red}[{green}+{red}]{reset_all}{white}"

banner = f"""{red}
This tool is for educational purposes only. Do not use it for illegal activities. 
The author is not responsible for misuse of this tool. By using this tool, you are fully responsible for your actions.

                                                          ███████████             ███████████              █████   
                                                         ░░███░░░░░███           ░░███░░░░░███            ░░███    
                                                          ░███    ░███ █████ ████ ░███    ░███   ██████   ███████  
                                                          ░██████████ ░░███ ░███  ░██████████   ░░░░░███ ░░░███░   
                                                          ░███░░░░░░   ░███ ░███  ░███░░░░░███   ███████   ░███    
                                                          ░███         ░███ ░███  ░███    ░███  ███░░███   ░███ ███
                                                          █████        ░░███████  █████   █████░░████████  ░░█████ 
                                                         ░░░░░          ░░░░░███ ░░░░░   ░░░░░  ░░░░░░░░    ░░░░░  
                                                                        ███ ░███                                   
                                                                       ░░██████                                    
                                                                        ░░░░░░                                                                                              
                                                                            {green}
                                                                                  v.{tool_version}
                                                                      {white}{github_url}    
{reset}"""

spacing = 40

category_01_text = f"{green}Network Attacks{red}"
category_02_text = f"{green}Web Applications{red}"
category_03_text = f"{green}OSINT{red}"
category_04_text = f"{green}Authentication and Credential{red}"
category_05_text = f"{green}Soon...{red}"

option_01_text = f"{white}[01] - Port Scanning{red}".ljust(spacing)
option_02_text = f"{white}[02] - ARP Spoofing{red}".ljust(spacing)
option_03_text = f"{white}[03] - DNS Spoofing{red}".ljust(spacing)
option_04_text = f"{white}[04] - MITM Attacks{red}".ljust(spacing)
option_05_text = f"{white}[05] - DDoS Attacks{red}".ljust(spacing)


option_06_text = f"{white}[06] - Subdomain Enumeration{red}".ljust(spacing)
option_07_text = f"{white}[07] - Directory Enumeration{red}".ljust(spacing)
option_08_text = f"{white}[08] - Domain Lookup{red}".ljust(spacing)
option_09_text = f"{white}[09] - Web Scraping{red}".ljust(spacing)
option_10_text = f"{white}[10] - SQL Injections{red}".ljust(spacing)
option_11_text = f"{white}[11] - XSS{red}".ljust(spacing)
option_12_text = f"{white}[12] - CSRF{red}".ljust(spacing)
option_13_text = f"{white}[13] - LFI/RFI{red}".ljust(spacing)
option_14_text = f"{white}[14] - Session{red}".ljust(spacing)


option_15_text = f"{white}[15] - Whois Lookup{red}".ljust(spacing)
option_16_text = f"{white}[16] - DNS Recon{red}".ljust(spacing)
option_17_text = f"{white}[17] - Social Media{red}".ljust(spacing)
option_18_text = f"{white}[18] - Google Dorking{red}".ljust(spacing)
option_19_text = f"{white}[19] - Metadata Extraction{red}".ljust(spacing)
option_20_text = f"{white}[20] - Email Lookup{red}".ljust(spacing)
option_21_text = f"{white}[21] - Email Tracker{red}".ljust(spacing)
option_22_text = f"{white}[22] - Phone Number Lookup{red}".ljust(spacing)
option_23_text = f"{white}[23] - GeoLocation{red}".ljust(spacing)

option_24_text = f"{white}[24] - Phishing{red}".ljust(spacing)
option_25_text = f"{white}[25] - Brute Force{red}".ljust(spacing)
option_26_text = f"{white}[26] - Hash Cracking{red}".ljust(spacing)


option_XX_text = f"{white}[XX] - Soon...{red}".ljust(spacing)

table_data = [
    [category_01_text, category_02_text, category_03_text, category_04_text, category_05_text],
    [option_01_text, option_06_text, option_15_text, option_24_text, option_XX_text],
    [option_02_text, option_07_text, option_16_text, option_25_text, ""],
    [option_03_text, option_08_text, option_17_text, option_26_text, ""],
    [option_04_text, option_09_text, option_18_text, "", ""],
    [option_05_text, option_10_text, option_19_text, "", ""],
    ["", option_11_text, option_20_text, "", ""],
    ["", option_12_text, option_21_text, "", ""],
    ["", option_13_text, option_22_text, "", ""],
    ["", option_14_text, option_23_text, "", ""]
]

option_01 = "port_scanning"
option_02 = "arp_spoofing"
option_03 = "dns_spoofing"
option_04 = "mitm_attacks"
option_05 = "ddos_attacks"


option_06 = "subdomain_enumeration"
option_07 = "directory_enumeration"
option_08 = "domain_lookup"
option_09 = "web_scraping"
option_10 = "sql_injections"
option_11 = "xss"
option_12 = "csrf"
option_13 = "lfi_rfi"
option_14 = "session"


option_15 = "whois_lookup"
option_16 = "dns_recon"
option_17 = "social_media"
option_18 = "google_dorking"
option_19 = "metadata_extraction"
option_20 = "email_lookup"
option_21 = "email_tracker"
option_22 = "phone_number_lookup"
option_23 = "geolocation"


option_24 = "phishing"
option_25 = "brute_force"
option_26 = "hash_cracking"

option_XX = "soon"

choices = {
    "01": option_01, "02": option_02, "03": option_03, "04": option_04, "05": option_05,
    "06": option_06, "07": option_07, "08": option_08, "09": option_09, "10": option_10, "11": option_11, "12": option_12, "13": option_13, "14": option_14,
    "15": option_15, "16": option_16, "17": option_17, "18": option_18, "19": option_19, "20": option_20, "21": option_21, "22": option_22, "23": option_23,
    "24": option_24, "25": option_25, "26": option_26,
    "XX": option_XX
}

categories = {
    "01": "Network_Attacks", "02": "Network_Attacks", "03": "Network_Attacks", "04": "Network_Attacks", "05": "Network_Attacks",
    "06": "Web_Applications", "07": "Web_Applications", "08": "Web_Applications", "09": "Web_Applications", "10": "Web_Applications", "11": "Web_Applications", "12": "Web_Applications", "13": "Web_Applications", "14": "Web_Applications",
    "15": "OSINT", "16": "OSINT", "17": "OSINT", "18": "OSINT", "19": "OSINT", "20": "OSINT", "21": "OSINT", "22": "OSINT", "23": "OSINT",
    "24": "Authentication_and_Credential", "25": "Authentication_and_Credential", "26": "Authentication_and_Credential",
    "XX": "Identity_and_Access"
}