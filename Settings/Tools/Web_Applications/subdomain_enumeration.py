from Settings.Utils import *

try:
    import concurrent.futures
    import tqdm
except ImportError:
    module_error()


def check_subdomain(domain: str, subdomain: str) -> bool:
    try:
        response = requests.get(f"https://{subdomain}.{domain}")

        if response.status_code == 200:
            return True
        else:
            return False

    except Exception as e:
        return False


def subdomain_enumeration(domain: str, wordlist: str) -> None:
    subdomains_list = open(f"{tool_path}Settings/Wordlists/Subdomains/{wordlist}").read().splitlines()

    # Remove lines with comments
    subdomains_list = [subdomain for subdomain in subdomains_list if not subdomain.startswith("#")]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(tqdm.tqdm(executor.map(check_subdomain, [domain] * len(subdomains_list), subdomains_list), total=len(subdomains_list)))

    print(f"\n{message_start} Subdomains found for {domain}:\n")

    if True not in results:
        print_message("No subdomains found.")
    else:
        for subdomain, status in zip(subdomains_list, results):
            if status:
                print(f"{bright}{green}   {subdomain}{reset_all}")

            
def main() -> None:
    print(banner)

    print(f"""{red}
                                                                ========================================
                                                                |{green}         Subdomain Enumeration        {red}|
                                                                ========================================          
    {reset_all}""")

    while True:
        domain = input(f"{message_start} Enter the IP address you want to lookup (or Q to quit): {reset_all}")

        if domain == "Q" or domain == "q":
            return
        
        if not validate_domain(domain):
            print(f"{error_start} Invalid domain or IP address.")
            continue

        wordlists = get_subdomains_wordlists()

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

    print(f"{message_start} Enumerating subdomains for {domain} with {wordlist} wordlist...\n")
    subdomain_enumeration(domain, wordlist)

    print("\n")
    wait_user()
