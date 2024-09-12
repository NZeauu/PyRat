from Settings.Utils import *

print(banner)

try:
    import dns.resolver

except ImportError:
    module_error()

def validate_domain(domain: str) -> bool:
    """Validate the domain entered by the user. 

    Args:
        domain (str): The domain to validate

    Returns:
        bool: True if the domain is valid, False otherwise
    """
    if domain.count(".") < 1:
        print_error("Invalid domain.")
        return False

    return True

def get_dns_record(domain: str):
    """Get the DNS records for a domain

    Args:
        domain (str): The domain to query
    """
    record_types = ["A", "AAAA", "NS", "MX", "TXT", "SOA", "CNAME", "PTR"]

    resolver = dns.resolver.Resolver()
    resolver.timeout = 10
    resolver.lifetime = 10
    
    for record in record_types:
        try:
            answers = resolver.resolve(domain, record)
            print("\n")
            print_message(f"{record}:")
            print(f"{green}{'-' * 30}{reset}")

            for server in answers:
                print_message(server.to_text())

        
        except dns.resolver.NoAnswer:
            print("\n")
            print_error(f"No {record} records found.")
            

        except dns.resolver.NXDOMAIN:
            print("\n")
            print_error(f"Domain {domain} does not exist.")
            return
        
        except dns.exception.Timeout:
            print("\n")
            print_error(f"DNS query for {record} timed out.")
            pass
        

def dns_recon_menu():
    """The main menu for the DNS Recon tool
    """
    print(f"""{red}
                                                                ========================================
                                                                |{green}             DNS Recon                {red}|
                                                                ========================================          
    {reset}""")

    while True:
        domain = input(f"{message_start} Enter the domain you want to query (or Q to quit): {reset}")

        if domain == "Q" or domain == "q":
            return
        
        elif validate_domain(domain):
            break

    get_dns_record(domain)
    wait_user()


try:
    dns_recon_menu()
except Exception as e:
    print_error(f"An error occurred: {e}")
    wait_user()
