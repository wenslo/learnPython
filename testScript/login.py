import requests

LOGIN_URL = 'http://47.105.99.73:8185/v1/aplus-jx-public/universal/user/authentication'

login_response = requests.post(LOGIN_URL, json={
    "loginName": "tjxadmin1",
    "password": "123456"
})
login_response = login_response.json()
print('Login resposne is %s' % login_response)
login_token = login_response['content']['token']
print('The login token is %s ' % login_token)

