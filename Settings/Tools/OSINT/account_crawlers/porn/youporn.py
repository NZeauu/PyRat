from Settings.Utils import *

def youporn(email: str) -> bool | None:
    """Youporn account crawler
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
    
        data = {
            'email': email,
        }

        check = session.post('https://www.youporn.com/register_validate', headers=headers, data=data)

        if check.status_code == 200:
            response = check.json()

            if response['success']:
                return False
            else:
                if response['messages'][0] == 'Email has been taken.':
                    return True
                else:
                    return None
        
    except Exception as e:
        return None