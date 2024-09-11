from Settings.Config import *
from Settings.Utils import *

try:
    import socket
    from concurrent.futures import ThreadPoolExecutor

except ImportError:
    module_error()
    exit()

print(banner)

# Function to scan a single port
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            try:
                port_service = socket.getservbyport(port)
                return f"Port {port}: Open (Service: {port_service})"
            except:
                return f"Port {port}: Open"
    except:
        pass

# Function to scan a range of ports
def scan_ports(ip):
    open_ports = []
    
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(65535 + 1)]
        for future in futures:
            result = future.result()
            if result:
                open_ports.append(result)
    
    return open_ports


def scanner_menu():
    # Make a large header for the port scanner title
    print(f"""{red}
                                                                ========================================
                                                                |{green}             Port Scanner             {red}|
                                                                ========================================          
    {reset}""")

    target = input(f"{red}[{green}+{red}]{white} Enter the target IP address (or Q to quit): {reset}")

    if target == "Q" or target == "q":
        return

    print(f"{red}[{green}+{red}]{white} Scanning ports on {target}...{reset}")
    open_ports = scan_ports(target)

    if len(open_ports) > 0:
        print(f"{red}[{green}+{red}]{white} Open ports on {target}:{reset}")
        for port in open_ports:
            print(f"    {port}")
    else:
        print(f"{red}[{green}+{red}]{white} No open ports found on {target}{reset}")

    input(f"{red}[{green}+{red}]{white} Press Enter to return to the main menu...{reset}")

    

scanner_menu()



