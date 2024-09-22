from Settings.Utils import *

def twitter(email):
    """Twitter account crawler
    """
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://twitter.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }
    data = {
        'email': email
    }

    try:
        session = requests.Session()
        r = session.get("https://api.twitter.com/i/users/email_available.json", headers=headers, params=data)

        if r.status_code == 200:
            check = r.json()
            if check['taken']:
                return True
            else:
                return False
            
        else:
            return None
        
    except Exception as e:
        return None