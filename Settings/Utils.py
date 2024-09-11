import os
import sys
from .Config import *

try:
    import subprocess
    import colorama

except ImportError:
    print(f"An error occurred while trying to import a module.")
    print(f"Please make sure you have all the necessary modules installed using requirements.txt or Setup.py.")
    print(f"If the problem persists, please contact the developer.")
    input(f"Press Enter to continue...")
    sys.exit()


tool_path = os.path.dirname(os.path.abspath(__file__)).split("Settings")[0].strip()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def start_tool(category, tool_name):
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
    print(f"An error occurred while trying to import a module.")
    print(f"Please make sure you have all the necessary modules installed using requirements.txt or Setup.py.")
    print(f"If the problem persists, please contact the developer.")
    input(f"Press Enter to continue...")
    return



# ======================================================================================================================
# |                                                     APP MENUS                                                      |
# ======================================================================================================================

red = colorama.Fore.RED
green = colorama.Fore.GREEN
white = colorama.Fore.WHITE
reset = colorama.Fore.RESET

banner = f"""{red}
This tool is for educational purposes only. Do not use it for illegal activities. 
The author is not responsible for misuse of this tool. By using this tool, you are fully responsible for your actions.

                                                                ██▓███ ▓██   ██▓ ██▀███   ▄▄▄     ▄▄▄█████▓
                                                                ▓██░  ██▒▒██  ██▒▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒
                                                                ▓██░ ██▓▒ ▒██ ██░▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░
                                                                ▒██▄█▓▒ ▒ ░ ▐██▓░▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ 
                                                                ▒██▒ ░  ░ ░ ██▒▓░░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ 
                                                                ▒▓▒░ ░  ░  ██▒▒▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   
                                                                ░▒ ░     ▓██ ░▒░   ░▒ ░ ▒░  ▒   ▒▒ ░   ░    
                                                                ░░       ▒ ▒ ░░    ░░   ░   ░   ▒    ░      
                                                                        ░ ░        ░           ░  ░        
                                                                        ░ ░                                
                                                                            {green}
                                                                                  v.{tool_version}
                                                                      {white}{github_url}    
                                    
         
{reset}"""

spacing = 40

category_01_text = f"{green}Network Attacks{red}".ljust(spacing)
category_02_text = f"{green}Web Applications{red}".ljust(spacing)
category_03_text = f"{green}OSINT{red}".ljust(spacing)
category_04_text = f"{green}Social Engineering{red}".ljust(spacing)
category_05_text = f"{green}Soon...{red}".ljust(spacing)

option_01_text = f"{white}[01] - Port Scanning{red}".ljust(spacing)
option_02_text = f"{white}[02] - ARP Spoofing{red}".ljust(spacing)
option_03_text = f"{white}[03] - DNS Spoofing{red}".ljust(spacing)
option_04_text = f"{white}[04] - MITM Attacks{red}".ljust(spacing)
option_05_text = f"{white}[05] - DDoS Attacks{red}".ljust(spacing)


option_06_text = f"{white}[06] - SQL Injections{red}".ljust(spacing)
option_07_text = f"{white}[07] - XSS{red}".ljust(spacing)
option_08_text = f"{white}[08] - CSRF{red}".ljust(spacing)
option_09_text = f"{white}[09] - LFI/RFI{red}".ljust(spacing)
option_10_text = f"{white}[10] - Session{red}".ljust(spacing)
option_11_text = f"{white}[11] - Web Scraping{red}".ljust(spacing)
option_12_text = f"{white}[12] - Directory Enumeration{red}".ljust(spacing)
option_13_text = f"{white}[13] - API Security{red}".ljust(spacing)
option_14_text = f"{white}[14] - Subdomain Enumeration{red}".ljust(spacing)


option_15_text = f"{white}[15] - Whois Lookup{red}".ljust(spacing)
option_16_text = f"{white}[16] - DNS Recon{red}".ljust(spacing)
option_17_text = f"{white}[17] - Social Media{red}".ljust(spacing)
option_18_text = f"{white}[18] - Google Dorking{red}".ljust(spacing)
option_19_text = f"{white}[19] - Public Records{red}".ljust(spacing)
option_20_text = f"{white}[20] - Email Lookup{red}".ljust(spacing)
option_21_text = f"{white}[21] - Phone Number Lookup{red}".ljust(spacing)
option_22_text = f"{white}[22] - GeoLocation{red}".ljust(spacing)
option_23_text = f"{white}[23] - People Search{red}".ljust(spacing)


option_24_text = f"{white}[24] - Phishing{red}".ljust(spacing)
option_25_text = f"{white}[25] - Baiting{red}".ljust(spacing)
option_26_text = f"{white}[26] - Pretexting{red}".ljust(spacing)
option_27_text = f"{white}[27] - Tailgating{red}".ljust(spacing)
option_28_text = f"{white}[28] - Impersonation{red}".ljust(spacing)
option_29_text = f"{white}[29] - Dumpster Diving{red}".ljust(spacing)
option_30_text = f"{white}[30] - Shoulder Surfing{red}".ljust(spacing)
option_31_text = f"{white}[31] - Elicitation{red}".ljust(spacing)
option_32_text = f"{white}[32] - Quizzes and Surveys{red}".ljust(spacing)


option_33_text = f"{white}[33] - Soon...{red}".ljust(spacing)


main_menu = f"""{red}
┌────────────────────────────────┬────────────────────────────────┬────────────────────────────────┬────────────────────────────────┬────────────────────────────────┐
│ {category_01_text            } │ {category_02_text            } │ {category_03_text            } │ {category_04_text            } │ {category_05_text            } │
├────────────────────────────────┼────────────────────────────────┼────────────────────────────────┼────────────────────────────────┼────────────────────────────────┤
│ {option_01_text              } │ {option_06_text              } │ {option_15_text              } │ {option_24_text              } │ {option_33_text              } │
│ {option_02_text              } │ {option_07_text              } │ {option_16_text              } │ {option_25_text              } │                                │
│ {option_03_text              } │ {option_08_text              } │ {option_17_text              } │ {option_26_text              } │                                │
│ {option_04_text              } │ {option_09_text              } │ {option_18_text              } │ {option_27_text              } │                                │
│ {option_05_text              } │ {option_10_text              } │ {option_19_text              } │ {option_28_text              } │                                │
│                                │ {option_11_text              } │ {option_20_text              } │ {option_29_text              } │                                │
│                                │ {option_12_text              } │ {option_21_text              } │ {option_30_text              } │                                │
│                                │ {option_13_text              } │ {option_22_text              } │ {option_31_text              } │                                │
│                                │ {option_14_text              } │ {option_23_text              } │ {option_32_text              } │                                │
└────────────────────────────────┴────────────────────────────────┴────────────────────────────────┴────────────────────────────────┴────────────────────────────────┘

{green}[Q]-Exit

{reset}"""

option_01 = "port_scanning"
option_02 = "arp_spoofing"
option_03 = "dns_spoofing"
option_04 = "mitm_attacks"
option_05 = "ddos_attacks"


option_06 = "sql_injections"
option_07 = "xss"
option_08 = "csrf"
option_09 = "lfi_rfi"
option_10 = "session"
option_11 = "web_scraping"
option_12 = "directory_enumeration"
option_13 = "api_security"
option_14 = "subdomain_enumeration"


option_15 = "whois_lookup"
option_16 = "dns_recon"
option_17 = "social_media"
option_18 = "google_dorking"
option_19 = "public_records"
option_20 = "email_lookup"
option_21 = "phone_number_lookup"
option_22 = "geolocation"
option_23 = "people_search"


option_24 = "phishing"
option_25 = "baiting"
option_26 = "pretexting"
option_27 = "tailgating"
option_28 = "impersonation"
option_29 = "dumpster_diving"
option_30 = "shoulder_surfing"
option_31 = "elicitation"
option_32 = "quizzes_surveys"


option_33 = "soon"

choices = {
    "01": option_01, "02": option_02, "03": option_03, "04": option_04, "05": option_05,
    "06": option_06, "07": option_07, "08": option_08, "09": option_09, "10": option_10, "11": option_11, "12": option_12, "13": option_13, "14": option_14,
    "15": option_15, "16": option_16, "17": option_17, "18": option_18, "19": option_19, "20": option_20, "21": option_21, "22": option_22, "23": option_23,
    "24": option_24, "25": option_25, "26": option_26, "27": option_27, "28": option_28, "29": option_29, "30": option_30, "31": option_31, "32": option_32,
    "33": option_33
}

categories = {
    "01": "Network_Attacks", "02": "Network_Attacks", "03": "Network_Attacks", "04": "Network_Attacks", "05": "Network_Attacks",
    "06": "Web_Applications", "07": "Web_Applications", "08": "Web_Applications", "09": "Web_Applications", "10": "Web_Applications", "11": "Web_Applications", "12": "Web_Applications", "13": "Web_Applications", "14": "Web_Applications",
    "15": "OSINT", "16": "OSINT", "17": "OSINT", "18": "OSINT", "19": "OSINT", "20": "OSINT", "21": "OSINT", "22": "OSINT", "23": "OSINT",
    "24": "Social_Engineering", "25": "Social_Engineering", "26": "Social_Engineering", "27": "Social_Engineering", "28": "Social_Engineering", "29": "Social_Engineering", "30": "Social_Engineering", "31": "Social_Engineering", "32": "Social_Engineering",
    "33": "Identity_and_Access"
}