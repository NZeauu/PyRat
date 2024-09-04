# ======================================================================================================================
# |                                                  APP CONSTANTS                                                     |
# ======================================================================================================================
tool_name = "PyRat"
tool_version = "1.0.0"
github_url = "https://github.com/NZeauu/PyRat"





# ======================================================================================================================
# |                                                  APP CONSTANTS                                                     |
# ======================================================================================================================
import colorama

red = colorama.Fore.RED
green = colorama.Fore.GREEN
white = colorama.Fore.WHITE
reset = colorama.Fore.RESET

banner = f"""{red}

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
category_05_text = f"{green}Identity and Access{red}".ljust(spacing)

option_01_text = f"{white}[01] - Port Scanning{red}".ljust(spacing)
option_02_text = f"{white}[02] - Network Mapping{red}".ljust(spacing)
option_03_text = f"{white}[03] - Packet Sniffing{red}".ljust(spacing)
option_04_text = f"{white}[04] - ARP Spoofing{red}".ljust(spacing)
option_05_text = f"{white}[05] - DNS Spoofing{red}".ljust(spacing)
option_06_text = f"{white}[06] - MITM Attacks{red}".ljust(spacing)
option_07_text = f"{white}[07] - Wireless Attacks{red}".ljust(spacing)
option_08_text = f"{white}[08] - DDoS Attacks{red}".ljust(spacing)
option_09_text = f"{white}[09] - Spoofing{red}".ljust(spacing)
option_10_text = f"{white}[10] - SQL Injections{red}".ljust(spacing)
option_11_text = f"{white}[11] - XSS{red}".ljust(spacing)
option_12_text = f"{white}[12] - CSRF{red}".ljust(spacing)
option_13_text = f"{white}[13] - LFI/RFI{red}".ljust(spacing)
option_14_text = f"{white}[14] - Session{red}".ljust(spacing)
option_15_text = f"{white}[15] - Web Scraping{red}".ljust(spacing)
option_16_text = f"{white}[16] - Directory{red}".ljust(spacing)
option_17_text = f"{white}[17] - API Security{red}".ljust(spacing)
option_18_text = f"{white}[18] - Subdomain{red}".ljust(spacing)
option_19_text = f"{white}[19] - Whois Lookup{red}".ljust(spacing)
option_20_text = f"{white}[20] - DNS Recon{red}".ljust(spacing)
option_21_text = f"{white}[21] - Social Media{red}".ljust(spacing)
option_22_text = f"{white}[22] - Google Dorking{red}".ljust(spacing)
option_23_text = f"{white}[23] - Public Records{red}".ljust(spacing)
option_24_text = f"{white}[24] - Email Lookup{red}".ljust(spacing)
option_25_text = f"{white}[25] - Phone Number Lookup{red}".ljust(spacing)
option_26_text = f"{white}[26] - GeoLocation{red}".ljust(spacing)
option_27_text = f"{white}[27] - People Search{red}".ljust(spacing)
option_28_text = f"{white}[28] - Phishing{red}".ljust(spacing)
option_29_text = f"{white}[29] - Baiting{red}".ljust(spacing)
option_30_text = f"{white}[30] - Pretexting{red}".ljust(spacing)
option_31_text = f"{white}[31] - Tailgating{red}".ljust(spacing)
option_32_text = f"{white}[32] - Impersonation{red}".ljust(spacing)
option_33_text = f"{white}[33] - Dumpster Diving{red}".ljust(spacing)
option_34_text = f"{white}[34] - Shoulder Surfing{red}".ljust(spacing)
option_35_text = f"{white}[35] - Elicitation{red}".ljust(spacing)
option_36_text = f"{white}[36] - Quizzes and Surveys{red}".ljust(spacing)
option_37_text = f"{white}[37] - IAM Policies{red}".ljust(spacing)
option_38_text = f"{white}[38] - User Roles{red}".ljust(spacing)
option_39_text = f"{white}[39] - MFA{red}".ljust(spacing)
option_40_text = f"{white}[40] - SSO{red}".ljust(spacing)
option_41_text = f"{white}[41] - Access Tokens{red}".ljust(spacing)
option_42_text = f"{white}[42] - Access Audits{red}".ljust(spacing)
option_43_text = f"{white}[43] - Access Control{red}".ljust(spacing)
option_44_text = f"{white}[44] - Key Management{red}".ljust(spacing)
option_45_text = f"{white}[45] - Password Policies{red}".ljust(spacing)

main_menu = f"""{red}
┌────────────────────────────────┬────────────────────────────────┬────────────────────────────────┬────────────────────────────────┬────────────────────────────────┐
│ {category_01_text            } │ {category_02_text            } │ {category_03_text            } │ {category_04_text            } │ {category_05_text            } │
├────────────────────────────────┼────────────────────────────────┼────────────────────────────────┼────────────────────────────────┼────────────────────────────────┤
│ {option_01_text              } │ {option_10_text              } │ {option_19_text              } │ {option_28_text              } │ {option_37_text              } │
│ {option_02_text              } │ {option_11_text              } │ {option_20_text              } │ {option_29_text              } │ {option_38_text              } │
│ {option_03_text              } │ {option_12_text              } │ {option_21_text              } │ {option_30_text              } │ {option_39_text              } │
│ {option_04_text              } │ {option_13_text              } │ {option_22_text              } │ {option_31_text              } │ {option_40_text              } │
│ {option_05_text              } │ {option_14_text              } │ {option_23_text              } │ {option_32_text              } │ {option_41_text              } │
│ {option_06_text              } │ {option_15_text              } │ {option_24_text              } │ {option_33_text              } │ {option_42_text              } │
│ {option_07_text              } │ {option_16_text              } │ {option_25_text              } │ {option_34_text              } │ {option_43_text              } │
│ {option_08_text              } │ {option_17_text              } │ {option_26_text              } │ {option_35_text              } │ {option_44_text              } │
│ {option_09_text              } │ {option_18_text              } │ {option_27_text              } │ {option_36_text              } │ {option_45_text              } │
└────────────────────────────────┴────────────────────────────────┴────────────────────────────────┴────────────────────────────────┴────────────────────────────────┘

{green}[Q]-Exit

{reset}"""

option_01 = "port_scanning"
option_02 = "network_mapping"
option_03 = "packet_sniffing"
option_04 = "arp_spoofing"
option_05 = "dns_spoofing"
option_06 = "mitm_attacks"
option_07 = "wireless_attacks"
option_08 = "ddos_attacks"
option_09 = "spoofing"
option_10 = "sql_injections"
option_11 = "xss"
option_12 = "csrf"
option_13 = "lfi_rfi"
option_14 = "session"
option_15 = "web_scraping"
option_16 = "directory"
option_17 = "api_security"
option_18 = "subdomain"
option_19 = "whois_lookup"
option_20 = "dns_recon"
option_21 = "social_media"
option_22 = "google_dorking"
option_23 = "public_records"
option_24 = "email_lookup"
option_25 = "phone_number_lookup"
option_26 = "geolocation"
option_27 = "people_search"
option_28 = "phishing"
option_29 = "baiting"
option_30 = "pretexting"
option_31 = "tailgating"
option_32 = "impersonation"
option_33 = "dumpster_diving"
option_34 = "shoulder_surfing"
option_35 = "elicitation"
option_36 = "quizzes_surveys"
option_37 = "iam_policies"
option_38 = "user_roles"
option_39 = "mfa"
option_40 = "sso"
option_41 = "access_tokens"
option_42 = "access_audits"
option_43 = "access_control"
option_44 = "key_management"
option_45 = "password_policies"


choices = {
    "01": option_01, "02": option_02, "03": option_03, "04": option_04, "05": option_05, "06": option_06, "07": option_07, "08": option_08, "09": option_09,
    "10": option_10, "11": option_11, "12": option_12, "13": option_13, "14": option_14, "15": option_15, "16": option_16, "17": option_17, "18": option_18,
    "19": option_19, "20": option_20, "21": option_21, "22": option_22, "23": option_23, "24": option_24, "25": option_25, "26": option_26, "27": option_27,
    "28": option_28, "29": option_29, "30": option_30, "31": option_31, "32": option_32, "33": option_33, "34": option_34, "35": option_35, "36": option_36,
    "37": option_37, "38": option_38, "39": option_39, "40": option_40, "41": option_41, "42": option_42, "43": option_43, "44": option_44, "45": option_45
}

categories = {
    "01": "Network_Attacks", "02": "Network_Attacks", "03": "Network_Attacks", "04": "Network_Attacks", "05": "Network_Attacks", "06": "Network_Attacks", "07": "Network_Attacks", "08": "Network_Attacks", "09": "Network_Attacks",
    "10": "Web_Applications", "11": "Web_Applications", "12": "Web_Applications", "13": "Web_Applications", "14": "Web_Applications", "15": "Web_Applications", "16": "Web_Applications", "17": "Web_Applications", "18": "Web_Applications",
    "19": "OSINT", "20": "OSINT", "21": "OSINT", "22": "OSINT", "23": "OSINT", "24": "OSINT", "25": "OSINT", "26": "OSINT", "27": "OSINT",
    "28": "Social_Engineering", "29": "Social_Engineering", "30": "Social_Engineering", "31": "Social_Engineering", "32": "Social_Engineering", "33": "Social_Engineering", "34": "Social_Engineering", "35": "Social_Engineering", "36": "Social_Engineering",
    "37": "Identity_and_Access", "38": "Identity_and_Access", "39": "Identity_and_Access", "40": "Identity_and_Access", "41": "Identity_and_Access", "42": "Identity_and_Access", "43": "Identity_and_Access", "44": "Identity_and_Access", "45": "Identity_and_Access"
}