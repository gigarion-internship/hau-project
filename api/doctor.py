import requests

baseURL = 'https://be-happydental.onrender.com/api/doctor/'

def getActiveDoctors():
    url = baseURL + 'active'
    res = requests.get(url)
    print(res.json())


def getDoctorById(id):
    if not type(id) is str:
        print('Doctor\'s ID must be string')
    else:
        url = baseURL + id
        res = requests.get(url)
        print(res.json())