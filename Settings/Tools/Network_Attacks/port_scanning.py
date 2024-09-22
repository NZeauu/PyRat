from Settings.Utils import *

print(banner)

try:
    import socket
    import concurrent.futures
    from tqdm import tqdm

except ImportError:
    module_error()

# Function to scan a single port
def scan_port(ip: str, port: int) -> str:
    """Scan a single port on a target IP address

    Args:
        ip (str): The target IP address
        port (int): The port to scan

    Returns:
        str: The result of the scan
    """
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
def scan_ports(ip: str) -> list:
    """Scan all ports on a target IP address

    Args:
        ip (str): The target IP address

    Returns:
        list: A list of open ports
    """
    open_ports = []
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(65535 + 1)]

        with tqdm(total=len(futures), desc="Scanning", unit="port") as pbar:
            for future in concurrent.futures.as_completed(futures):
                pbar.update(1)
                result = future.result()
                if result:
                    open_ports.append(result)
    
    return open_ports


def scanner_menu():
    """Port scanner menu
    """
    # Make a large header for the port scanner title
    print(f"""{red}
                                                                ========================================
                                                                |{green}             Port Scanner             {red}|
                                                                ========================================          
    {reset}""")


    while True:
        target = input(f"{message_start} Enter the target IP address (or Q to quit): {reset}")
        
        if target == "Q" or target == "q":
            return
        
        elif validate_ip(target):
            break

    print_message(f"Scanning ports on {target}...")
    open_ports = scan_ports(target)

    if len(open_ports) > 0:
        print("\n")
        print_message(f"Open ports on {target}:")
        for port in open_ports:
            print(f"    {port}")
    else:
        print_message(f"No open ports found on {target}")

    wait_user()

try:
    scanner_menu()
except Exception as e:
    print_error(f"An error occurred: {e}")
    wait_user()


