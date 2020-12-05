import requests
import RPi.GPIO as GPIO
import time

pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

key = "44bac61c7ab1d1fef3a2b0820afdc093"
lat = '43.0832242'
lon = '-89.3815317'
city = "madison"
state = "WI"
url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={key}'
print(url)
response = requests.get(url).json()
print(response['weather'][0]['description'])
print(response['main']['temp'])
if True:
    GPIO.output(pin, True)
    time.sleep(1)
    GPIO.output(pin, False)

GPIO.cleanup()
