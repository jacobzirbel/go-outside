from datetime import datetime
monthlyWeather = [
    ["January", 27, 8],
    ["February", 31, 11],
    ["March", 44, 23],
    ["April", 58, 34],
    ["May", 70, 45],
    ["June", 79, 54],
    ["July", 83, 59],
    ["August", 81, 57],
    ["September", 74, 48],
    ["October", 61, 37],
    ["November", 46, 27],
    ["December", 32, 14],
]

def shouldGoOutside(currentTemp, date = datetime.today()):
    monthIndex = date.month - 1
    return currentTemp > monthlyWeather[monthIndex][1]
