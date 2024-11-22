from Settings.Utils import *

def plurk(email: str) -> bool | None:
    """Plurk account crawler
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': '*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.plurk.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

    data = {
        'email': email
    }

    try:
        session = requests.Session()
        check = session.post('https://www.plurk.com/Users/isEmailFound', headers=headers, data=data)

        if check.status_code == 200:
            if check.text == "True":
                return True
            else:
                return False
        else:
            return None
    except Exception as e:
        return None
    