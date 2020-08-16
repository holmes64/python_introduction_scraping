import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Tokyo,JP", key="api_key")

jsondata = requests.get(url).json()
print("都市名  =", jsondata["name"])
print("気温  =", jsondata["main"]["temp"])
print("天気  =", jsondata["weather"][0]["main"])
print("天気詳細  =", jsondata["weather"][0]["description"])
