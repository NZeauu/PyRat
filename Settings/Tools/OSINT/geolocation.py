from Settings.Utils import *

def geolocation(ip: str) -> None:
    """Geolocation tool

    Args:
        ip (str): The IP address to locate
    """
    url = f"http://ip-api.com/json/{ip}"

    try:
        response = requests.get(url)
        ip_location = response.json()

        print(f"{bright}{green} IP: {reset_all}{ip}")
        print(f"{bright}{green} Country: {reset_all}{ip_location['country']} ({ip_location['countryCode']})")
        print(f"{bright}{green} Region: {reset_all}{ip_location['regionName']}")
        print(f"{bright}{green} City: {reset_all}{ip_location['city']}")
        print(f"{bright}{green} ZIP: {reset_all}{ip_location['zip']}")
        print(f"{bright}{green} Latitude: {reset_all}{ip_location['lat']}")
        print(f"{bright}{green} Longitude: {reset_all}{ip_location['lon']}")
        print(f"{bright}{green} ISP: {reset_all}{ip_location['isp']}")
        print(f"{bright}{green} AS: {reset_all}{ip_location['as']}")
        print(f"{bright}{green} Timezone: {reset_all}{ip_location['timezone']}")
        print(f"{bright}{green} Organization: {reset_all}{ip_location['org']}")    

        print(f"\n{bright}{green}You can see the location on the map by visiting the following link:{reset_all}")
        print(f"{bright}{blue}https://www.google.com/maps/place/{ip_location['lat']},{ip_location['lon']}{reset_all}")

    except Exception as e:
        print_error(f"An error occurred: {e}")
        return
    

def main() -> None:
    print(banner)

    print(f"""{red}
                                                                ========================================
                                                                |{green}              Geolocation             {red}|
                                                                ========================================          
    {reset}""")

    while True:
        ip = input(f"{message_start} Enter the IP address you want to locate (or Q to quit): {reset}")

        if ip == "Q" or ip == "q":
            return
        
        elif validate_ip(ip):
            break

    geolocation(ip)

    wait_user()

