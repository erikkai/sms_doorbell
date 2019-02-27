import RPi.GPIO as GPIO
import time
from requests.auth import HTTPBasicAuth
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

url = 'https://rest-ww.telesign.com/v1/messaging' 
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/x-www-form-urlencoded'}

# Replace 'Your phone number goes here' with the complete phone number, including the country code and no special characters 
# or spaces. 

data = {'phone_number': 'Your phone number goes here.', ‘message_type’:’ARN’, ‘message': 'Someone is at the door.'}
while True:
    input_state = GPIO.input(18)
    if input_state == False:
        r = requests.post(url, auth=HTTPBasicAuth(‘Your customer ID goes here', 'Your API key goes here'), data=data, headers=headers)
        print('Button Pressed')
        time.sleep(0.2)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
