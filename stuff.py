import requests
import RPi.GPIO as GPIO
import time
from datetime import datetime

from util import shouldGoOutside

pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

key = "44bac61c7ab1d1fef3a2b0820afdc093"
lat = '43.0832242'
lon = '-89.3815317'
city = "madison"
state = "WI"
url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={key}'

print(datetime.today())

response = requests.get(url).json()
print(response['weather'][0]['description'])
temp = response['main']['feels_like']
print("Feels like: %s" % temp)

lightOn = shouldGoOutside(temp)
if lightOn:
    print("Turning light on")
else:
    print("Turning light off")
GPIO.output(pin, lightOn)

#GPIO.cleanup()
