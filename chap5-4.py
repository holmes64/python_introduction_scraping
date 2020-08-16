import requests
import json
from pprint import pprint

url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Kobe,JP", key="api_key")

jsondata = requests.get(url).json()
pprint(jsondata)
