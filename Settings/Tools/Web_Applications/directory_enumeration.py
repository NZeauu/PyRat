from Settings.Utils import *

try:
    import concurrent.futures
    import tqdm
except ImportError:
    module_error()


def check_directory(domain: str, directory: str) -> bool:
    try:
        response = requests.get(f"https://{domain}/{directory}/")

        if response.status_code == 200 or response.status_code == 403:
            return True
        else:
            return False

    except Exception as e:
        return False

def directory_enumeration(domain: str, wordlist: str) -> None:
    directory_list = open(f"{tool_path}Settings/Wordlists/Directories/{wordlist}").read().splitlines()

    # Remove lines with comments
    directory_list = [directory for directory in directory_list if not directory.startswith("#")]

    results = []
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for result in tqdm.tqdm(executor.map(check_directory, [domain] * len(directory_list), directory_list), total=len(directory_list)):
                results.append(result)
    except KeyboardInterrupt:
        print("\nKeyboard interruption detected. Displaying current results...\n")

    print(f"\n{message_start} Directories found for {domain}:\n")

    if True not in results:
        print_message("No directories found.")
    else:
        for directory, status in zip(directory_list, results):
            if status:
                print(f"{bright}{green}   {directory}{reset_all}")

            
def main() -> None:
    print(banner)

    print(f"""{red}
                                                                ========================================
                                                                |{green}         Directory Enumeration        {red}|
                                                                ========================================          
    {reset_all}""")

    while True:
        domain = input(f"{message_start} Enter the IP address you want to lookup (or Q to quit): {reset_all}")

        if domain == "Q" or domain == "q":
            return
        
        if not validate_domain(domain):
            print(f"{error_start} Invalid domain or IP address.")
            continue

        wordlists = get_directories_wordlists()

        for idx, wordlist in enumerate(wordlists):
            print(f"    {idx+1}. {wordlist}")

        wordlist_choice = input(f"{message_start} Enter the number of the wordlist you want to use: {reset_all}")
    
        if not wordlist_choice.isdigit():
            print(f"{error_start} Invalid choice.")
            continue
        else:
            wordlist_choice = int(wordlist_choice)

            if wordlist_choice < 1 or wordlist_choice > len(wordlists):
                print(f"{error_start} Invalid choice.")
                continue

            wordlist = wordlists[wordlist_choice - 1]

            break

    print(f"{message_start} Enumerating directories for {domain} with {wordlist} wordlist...\n")
    directory_enumeration(domain, wordlist)

    print("\n")
    input("Press Enter to continue...")