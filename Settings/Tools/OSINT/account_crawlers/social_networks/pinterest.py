from Settings.Utils import *

def pinterest(email):
    """Pinterest account crawler
    """

    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Connection': 'keep-alive',
        }

        session = requests.Session()
        r = session.get("https://www.pinterest.com/resource/EmailExistsResource/get/",
                headers=headers,
                params={
                    "data": '{"options": {"email": "' + email + '"} }'
                }
        )
        check = r.json()

        if check['resource_response']['data']:
            return True
        else:
            return False

    except Exception as e:
        return None
    