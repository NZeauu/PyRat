from Settings.Utils import *

def imgur(email: str) -> bool | None:
    """Imgur account crawler
    """
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://imgur.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }
    data = {
        'email': email
    }

    try:
        check = requests.post(
            "https://imgur.com/signin/ajax_email_available",
            data=data,
            headers=headers)
        check = check.json()

        if not check['data']['available']:
            return True
        else:
            return False
    except Exception as e:
        return None
