import requests
import json
import pandas as pd
from pprint import pprint
from datetime import datetime, timedelta, timezone

'''
    Source: https://openweathermap.org/forecast5
'''

url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Tokyo,JP", key="api_key")

jsondata = requests.get(url).json()
# pprint(jsondata)

df = pd.DataFrame(columns=["気温"])
tz = timezone(timedelta(hours=+9), 'JST')
for dat in jsondata["list"]:
    jst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9]
    weather = dat["weather"][0]["description"]
    temp = dat["main"]["temp"]
    # print("日時:{jst}, 天気:{w}, 気温:{t}度".format(jst=jst, w=weather, t=temp))
    df.loc[jst] = temp

pprint(df)
