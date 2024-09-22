from Settings.Utils import *

def wattpad(email):
    """Wattpad account crawler
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': '*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Referer': 'https://www.wattpad.com/',
        'TE': 'Trailers',
        'X-Requested-With': 'XMLHttpRequest',
    }
    params = {
        'email': email
    }

    try:
        r = requests.get("https://www.wattpad.com/api/v3/users/validate", headers=headers, params=params)
        if r.status_code == 400:
            return True
        else:
            return False

    except Exception as e:
        return None
    