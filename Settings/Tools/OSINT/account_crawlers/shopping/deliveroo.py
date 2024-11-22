from Settings.Utils import *

def deliveroo(email: str) -> bool | None:
    """Deliveroo account crawler
    """
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://deliveroo.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }
    data = {
        'email_address': email
    }

    try: 
        client = httpx.Client()
        check = client.post(
            "https://api.fr.deliveroo.com/consumer/accounts/check-email",
            json=data,
            headers=headers
        )
        
        check = check.json()

        if check['registered']:
            return True
        else:
            return False
        
    except Exception as e:
        return None