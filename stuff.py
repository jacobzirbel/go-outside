import requests
import RPi.GPIO as G
import time

pin = 4
G.setmode(G.BCM)
G.setup(pin, G.OUT)

key = "44bac61c7ab1d1fef3a2b0820afdc093"
city = "madison"
state = "WI"
url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={key}'
print(url)
response = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=43.0731&lon=-89.4012&units=imperial&appid=44bac61c7ab1d1fef3a2b0820afdc093').json()
print(response['weather'][0]['description'])
print(response['main']['temp'])
if True:
    G.output(pin, False)
    time.sleep(1)

