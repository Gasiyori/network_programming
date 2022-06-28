# json 포맷으로 post하고 결과값에서 특정 항목 분리하는 문제였던 것 같음.

import requests
import json

url = 'https://httpbin.org/post'
data = {'ID': '20171520', 'Name': 'Giyeong Hong', "Department": "IoT"}

rsp = requests.post(url, json=data)
print(rsp.text)

temp = json.loads(rsp.text)
print(temp['json'])