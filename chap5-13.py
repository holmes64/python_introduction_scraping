import requests
import json
import pandas as pd
from pprint import pprint
from datetime import datetime, timedelta, timezone
import matplotlib.pyplot as plt
import japanize_matplotlib


url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Tokyo,JP", key="api_key")

jsondata = requests.get(url).json()
df = pd.DataFrame(columns=["気温"])
tz = timezone(timedelta(hours=+9), 'JST')

for dat in jsondata["list"]:
    jst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9]
    weather = dat["weather"][0]["description"]
    temp = dat["main"]["temp"]
    df.loc[jst] = temp

df.plot(figsize=15, 8)
plt.ylim(-10, 40)
plt.grid()
