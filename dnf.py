import requests
from datetime import datetime, timedelta
import json
import pandas as pd
import os
API_KEY = os.getenv("DNF_API_KEY")
kor_last_time = datetime.now() - timedelta(days=1) #1일 전 코드
kor_last_time = kor_last_time.strftime("%Y%m%dT%H%M%S")
kor_time = datetime.now()
kor_time = kor_time.strftime("%Y%m%dT%H%M%S")
params = {
    "code" : "505",
    "apikey" : API_KEY,
    "limit" : 100,
    "startDate" : kor_last_time,
    "endDate" : kor_time
}
data = requests.get("https://api.neople.co.kr/df/servers/cain/characters/a7a19fdce357c1c83d48e80c66bf210a/timeline", params= params).json()
item_date = data['timeline']['rows']
item_data = data['timeline']['rows']
item_data
item_list = []
try:
    for i in item_data:
        b= i['data']
        b['date'] = i['date']
        item_list.append(b)
    df = pd.DataFrame(item_list)
    df = df.sort_values('date', ascending=True)
    if os.path.exists("item_data.csv"):
        df.to_csv("item_data.csv", mode='a', header=False, index=False, encoding='CP949')
    else:   
        df.to_csv("item_data.csv", mode='a', header=True, index=False, encoding='CP949')
except:
    pass
