from Settings.Utils import *

def adobe(email):
    """Adobe account crawler
    """
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-IMS-CLIENTID': 'adobedotcom2',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://auth.services.adobe.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

    data = {
        'username': email,
        "usernameType": "EMAIL"
    }

    try:
        session = requests.Session()
        check = session.post('https://auth.services.adobe.com/signin/v2/users/accounts', headers=headers, json=data)

        if check.text != "[]":
            return True
        else:
            return False
        
    except Exception as e:
        return None
    