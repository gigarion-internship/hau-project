import requests

baseURL = 'https://be-happydental.onrender.com/api/auth/'

def loginAdmin():
    url = baseURL + 'login/admin'
    loginData = {
        'role': 2,
        'email': 'lethihau.d19@gmail.com',
        'password': '123456'
    }
    res = requests.post(url, json=loginData)
    data = res.json()
    errCode = data['errCode']
    message = data['message']
    
    if errCode == 0:
        print(data)
    else:
        print('Error code: ', errCode)
        print('Error message: ', message)

loginAdmin()