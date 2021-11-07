# Create.main.py
# weather.main.py
# used OpenWeatherMap_API "https://openweathermap.org/"

import requests


def weatherSet():

    params = {"q": "Tokyo", "appid": "706a6848e95d332c4d575e7d8d2ac78e"}
    url = "http://api.openweathermap.org/data/2.5/forecast"
    res = requests.get(url, params=params)

    jsonText = res.json()

    print(end="\n--------------\n")

    for i in range(0, 5):  # 0,1,2,3,4

        print("気温:", jsonText["list"][i]["main"]["temp"])  # 気温はケルビン表示
        print("湿度:", jsonText["list"][i]["main"]["humidity"])
        print("天気:", jsonText["list"][i]["weather"][0]["main"])
        print("風速:", jsonText["list"][i]["wind"]["speed"])
        print("日時", jsonText["list"][i]["dt_txt"], end="\n--------------\n")


weatherSet()