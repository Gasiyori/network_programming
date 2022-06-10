import requests

url = 'https://httpbin.org/post'
data = {'IoT': '2017'}

rsp = requests.post(url, data=data)
print(rsp.text)

rsp = requests.post(url, json=data)
print(rsp.text)

files = {'file': open('iot.png', 'rb')} # 이미지 필요
rsp = requests.post(url, files=files)
print(rsp.text)