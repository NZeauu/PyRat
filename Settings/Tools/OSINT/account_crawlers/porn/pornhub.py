from Settings.Utils import *

try:
    from bs4 import BeautifulSoup
except ImportError:
    module_error()

def pornhub(email):
    
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
        r = session.get("https://www.pornhub.com/", headers=headers)

        soup = BeautifulSoup(r.text, 'html.parser')

        # Find the value of 'token' in a script block
        scripts = soup.find_all('script')

        for script in scripts:
            if "token" in script.text:
                text = script.text.split("token = '")[0]
                token_match = re.search(r'token\s*=\s*"([^"]+)"', text)

                if token_match:
                    token = token_match.group(1)
                    break

        
        params = {
            'token': token,
        }

        data = {
            'check_what': 'email',
            'email': email,
        }


        check = session.post('https://www.pornhub.com/user/create_account_check', headers=headers, params=params, data=data)

        if check.status_code == 200:
            response = check.json()

            if response['error_message'] == 'Email has been taken.':
                return True
            else:
                return False
        
    except Exception as e:
        return None
    