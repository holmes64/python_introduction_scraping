import requests
import json
from pprint import pprint
from datetime import datetime, timedelta, timezone

url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}"
url = url.format(city="Tokyo,JP", key="api_key")

jsondata = requests.get(url).json()
# pprint(jsondata)

tz = timezone(timedelta(hours=+9), 'JST')
for dat in jsondata["list"]:
    jst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9]
    print("UST={ust}, JST={jst}".format(ust=dat["dt_txt"], jst=jst))
