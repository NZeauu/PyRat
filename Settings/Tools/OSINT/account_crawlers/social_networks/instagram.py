from Settings.Utils import *

def instagram(email: str) -> bool | None:
    """Instagram account crawler
    """
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://www.instagram.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }
    data = {
        'email': email
    }

    try:
        session = requests.Session()
        r = session.get("https://www.instagram.com/accounts/emailsignup/", headers=headers)
        if r.status_code == 200:
            if 'csrftoken' in session.cookies:
                token = session.cookies['csrftoken']
            else:
                return None
        else:
            return None

    except Exception as e:
        return None

    headers['X-CSRFToken'] = token

    try:

        check = requests.post(
            "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/",
            data=data,
            headers=headers
        )
        if check.status_code != 200:
            return None
        
        check = check.json()

        if check['account_created'] == False:
            if "email" in check["errors"]:
                if check['errors']['email'][0]['code'] == 'email_is_taken':
                    return True
                else:
                    return None
            else:
                return False
        else:
            return None
        
    except Exception as e:
        return None
    