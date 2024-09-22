from Settings.Utils import *

try:
    from bs4 import BeautifulSoup
except ImportError:
    module_error()

def tumblr(email):
    """Tumblr account crawler
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': '*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.tumblr.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

    data = {
        'email': email
    }

    try:
        session = requests.Session()

        getBearer = session.get("https://www.tumblr.com/", headers=headers)
        if getBearer.status_code != 200:
            raise Exception("xc")
        

        # Find the value "API_TOKEN" in the HTML response for the Bearer token (Authorization)
        soup = BeautifulSoup(getBearer.text, 'html.parser')
        for script in soup.find_all('script'):
            if "API_TOKEN" in script.text:
                text = script.text.split("API_TOKEN = '")[0]
                match = re.search(r'"API_TOKEN":"(.*?)"', text)
                if match:
                    api_token = match.group(1)
                    headers['Authorization'] = 'Bearer ' + api_token
                break

    except Exception as e:
        return None

    try:
        session = requests.Session()
        check = session.post('https://www.tumblr.com/api/v2/user/validate', headers=headers, data=data)

        if check.status_code == 400:

            response = check.json()
            if response['response']["user_errors"][0]['code'] == 2:
                return True
            else:
                return None
        else:
            return False
        
    except Exception as e:
        return None
    