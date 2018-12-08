import json

import requests

LOGIN_URL = 'www.baidu.com'

login_response = requests.post(LOGIN_URL, json={
    "username": "username",
    "password": "password"
})
login_response = login_response.json()
login_response_formatted = json.dumps(response, sort_keys=True, indent=4, separators=(',', ':'))

print('Login resposne is %s' % login_response_formatted)
login_token = login_response['token']
print('The login token is %s ' % login_token)

headers = {'token': login_token}
