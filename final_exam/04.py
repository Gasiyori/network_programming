from urllib import request
import requests
import re

url = 'https://home.sch.ac.kr/iot/'
rsp = requests.get(url)
html = rsp.text

result = re.findall(r'([\w.]+)(@)(.+)(\.[a-z]{2,3})', html)
print(''.join(result[0]))

result = re.findall(r'\d{3}-\d{3,4}-\d{4}', html) # (3) - (3 ~ 4) - (4) 형태
for x in result:
    print(x)