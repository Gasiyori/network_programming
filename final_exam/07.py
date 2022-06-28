import requests
import json

url = 'https://httpbin.org/post'
data = {'ID': '20171520', 'Name': 'Giyeong Hong', "Department": "IoT"}

rsp = requests.post(url, json=data)
print(rsp.text)

temp = json.loads(rsp.text)
print(temp['json'])