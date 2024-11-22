from Settings.Utils import *

def duolingo(email: str) -> bool | None:
    """Duolingo account crawler
    """
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://www.duolingo.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

    try:
        check = requests.get(
            "https://www.duolingo.com/2017-06-30/users?email="+email,
            headers=headers)
        check = check.json()

        if check['users']:
            return True
        else:
            return False

    except Exception as e:
        return None
    