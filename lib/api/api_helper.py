import requests
from lib.Helpers.helpers import mylogger


def get(url, token=None):
    headers = {
        'Authorization': token
    }
    response = requests.get(url, headers=headers)
    request_url = response.request
    request_headers = response.headers
    # request log
    mylogger(f"{request_url, request_headers}")
    # response log
    mylogger(f'{response.json()}')
    return response.json()



def post(url, payload, token=None):
    headers = {
        'Authorization': token
    }
    response = requests.post(url, headers=headers, json=payload)
    request_url = response.url
    request_headers = response.headers
    # request log
    mylogger(f"{request_url, request_headers}")
    # response log
    mylogger(f'{response.json()}')
    return response.json()

#
def put(url, payload, token=None):
    headers = {
        'Authorization': token
    }
    response = requests.put(url, headers=headers, json=payload)
    request_url = response.url
    request_headers = response.headers
    # request log
    mylogger(f"{request_url, request_headers}")
    # response log
    mylogger(f'{response.json()}')
    return response.json()


