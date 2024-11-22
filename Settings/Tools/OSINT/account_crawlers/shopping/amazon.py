from Settings.Utils import *

try:
    from bs4 import BeautifulSoup
except ImportError:
    module_error()

def amazon(email: str) -> bool:
    """Amazon account crawler
    """
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try: 
        # session = requests.Session()
        client = httpx.Client()
        url = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"

        call = client.get(url, headers=headers)
        body = BeautifulSoup(call.text, 'html.parser')
        data = dict([(x["name"], x["value"]) for x in body.select(
            'form input') if ('name' in x.attrs and 'value' in x.attrs)])
        data["email"] = email

        check = client.post(
            "https://www.amazon.com/ap/signin",
            data=data
        )
        soup = BeautifulSoup(check.text, 'html.parser')

        if soup.find('div', {'id': 'auth-password-missing-alert'}):
            return True
        else:
            return False
        
    except Exception as e:
        return None
    