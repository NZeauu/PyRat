from Settings.Utils import *

def spotify(email):
    """Spotify account crawler
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

    params = {
        'validate': '1',
        'email': email,
    }


    try:
        response = requests.get(
            'https://spclient.wg.spotify.com/signup/public/v1/account',
            headers=headers,
            params=params
        )

        if response.status_code == 200:
            check = response.json()

            if check['status'] == 1:
                return False
            elif check['status'] == 20:
                return True
            
        else:
            return None
    except:
        return None
    