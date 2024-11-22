from Settings.Utils import *

try:
    import phonenumbers
    from phonenumbers import geocoder, carrier
    from phonenumbers import timezone
    from phonenumbers import PhoneNumberType
    from phonenumbers import PhoneNumberFormat

except ImportError:
    module_error()


def phone_number_lookup(phone_number: str) -> None:
    """Phone number lookup tool

    Args:
        phone_number (str): The phone number to lookup
    """
    try:
        phone_number = phonenumbers.parse(phone_number, None)

        print(f"{bright}{green} Phone number: {reset_all}{phonenumbers.format_number(phone_number, PhoneNumberFormat.INTERNATIONAL)}")
        print(f"{bright}{green} Country code: {reset_all}{phone_number.country_code}")
        print(f"{bright}{green} National number: {reset_all}{phone_number.national_number}")
        print(f"{bright}{green} Country: {reset_all}{geocoder.description_for_number(phone_number, 'en')}")
        print(f"{bright}{green} Carrier: {reset_all}{carrier.name_for_number(phone_number, 'en')}")
        print(f"{bright}{green} Timezone: {reset_all}{timezone.time_zones_for_number(phone_number)}")

    except Exception as e:
        print_error(f"An error occurred: {e}")
        return
    

def main() -> None:
    print(banner)

    print(f"""{red}
                                                                ========================================
                                                                |{green}          Phone Number Lookup         {red}|
                                                                ========================================          
    {reset}""")

    while True:
        phone_number = input(f"{message_start} Enter the phone number you want to lookup with the country code (or Q to quit): {reset}")

        if phone_number == "Q" or phone_number == "q":
            return
        
        elif not phone_number.startswith("+"):
            print_error("Invalid phone number. Please try again.")
            continue

        elif not phonenumbers.is_possible_number(phonenumbers.parse(phone_number, None)):
            print_error("Invalid phone number. Please try again.")
            continue

        else:
            break

    phone_number_lookup(phone_number)

    wait_user()
