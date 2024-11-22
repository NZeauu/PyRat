from Settings.Utils import *

def xvideos(email: str) -> bool | None:
    """Xvideos account crawler
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en,en-US;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    try:
        session = requests.Session()


        params = {
            'email': email
        }

        check = session.post('https://www.xvideos.com/account/checkemail', headers=headers, params=params)

        if check.status_code == 200:
            response = check.json()
            if not response['result'] and response['code'] == 1:
                return True
            else:
                return False
        
    except Exception as e:
        return None
    