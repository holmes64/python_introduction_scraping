import requests
import json
from pprint import pprint

# ans = "今日は{key1}です。明日は{key2}です。"
# print(ans)

# ans = ans.format(key1="晴れ", key2="曇り")
# print(ans)

url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Kobe,JP", key="api_key")

jsondata = requests.get(url).json()
print(jsondata)



