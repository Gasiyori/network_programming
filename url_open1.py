from urllib import request

rsp = request.urlopen('https://home.sch.ac.kr/iot')
print('HTTP Response:', rsp) # rsp 객체 위치
print('URL:', rsp.geturl())  # 홈페이지 주소
print('Status:', rsp.getcode()) # 상태

headers = rsp.info()
print('Date:', headers['date']) # 헤더에서 날짜, 시각
print('Headers')
print('-------------')
print(headers) # 헤더 전체 내용

data = rsp.read().decode()
print('Length:', len(data))
print('Data')
print('-------------')
print(data)