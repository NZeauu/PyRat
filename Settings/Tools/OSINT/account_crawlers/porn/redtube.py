from Settings.Utils import *


def redtube(email):
        
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
            r = session.get("https://www.redtube.com/", headers=headers)
    
            # Find the value of 'page_params.token' in a script block
            scripts = r.text.split('<script>')
    
            for script in scripts:
                if "page_params.token" in script:
                    text = script.split("page_params.token = '")[0]
                    token_match = re.search(r'page_params.token\s*=\s*"([^"]+)"', text)
    
                    if token_match:
                        token = token_match.group(1)
                        break
    
            
            headers['X-Requested-With'] = 'XMLHttpRequest'            

            params = {
                'token': token,
            }
    
            data = {
                'token': token,
                'redirect': '',
                'check_what': 'email',
                'email': email,
            }
    
    
            check = session.post('https://www.redtube.com/user/create_account_check', headers=headers, params=params, data=data)
    
            if check.status_code == 200:
                response = check.json()
    
                if response['error_message'] == 'Email has been taken.':
                    return True
                else:
                    return False
            
        except Exception as e:
            return None
        