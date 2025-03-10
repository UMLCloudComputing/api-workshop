"""
Developer: Christopher Coco 
This file shows off the Dexcom Share API and making a request with user credientials to get current EGV.
All information about the API can be found at https://gist.github.com/StephenBlackWasAlreadyTaken/adb0525344bedade1e25.
"""
from const import *
import requests
import maskpass
import json

print('Dexcom Share API Example')
username = input('Enter your username: ')
password = maskpass.askpass('Enter your password: ')

body = {
    'accountName': username,
    'password': password,
    'applicationId': APPLICATION_ID,
}

res = requests.post(BASE_URL_US+LOGIN_ENDPOINT, headers={'Content-Type': 'application/json'}, json=body)
session_id = res.content.decode().replace('"', '')

params = {
    'sessionId': session_id,
    'maxCount': 1,
    'minutes': DEFAULT_MINUTES,
}

res = requests.post(BASE_URL_US+CURRENT_EGV_ENDPOINT, params=params)
data = json.loads(res.content.decode().replace('[','').replace(']',''))

print(f'{data['Value']} {TTREND_ARROW_MAP[data['Trend']]}')