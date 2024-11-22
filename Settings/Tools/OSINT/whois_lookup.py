from Settings.Utils import *

try:
    from ipwhois import IPWhois

except ImportError:
    module_error()

def main() -> None:
    """IP Lookup (WhoIs) tool
    """
    print(banner)

    print(f"""{red}
                                                                ========================================
                                                                |{green}             IP Lookup (WhoIs)        {red}|
                                                                ========================================          
    {reset}""")

    while True:
        ip = input(f"{message_start} Enter the IP address you want to lookup (or Q to quit): {reset}")

        if ip == "Q" or ip == "q":
            return
        
        elif validate_ip(ip):
            break

    obj = IPWhois(ip)
    res = obj.lookup_whois()
    
    print("\n")
    print(f"{message_start}{bright} Results:{reset_all}\n")

    for key, value in res.items():
        if value is not None:
            if key == "nets":
                print(f"\n{message_start} Subnets:{reset}")
                for subnet in value:
                    for k, v in subnet.items():
                        if v is not None:
                            print(f"{red}{k}{reset}: {v}")

                print("\n")
            else:
                print(f"{red}{key}{reset}: {value}")


    wait_user()
