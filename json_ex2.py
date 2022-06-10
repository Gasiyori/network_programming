import json

# 다음과 같은 json 데이터 생성
dict_data = {'Name': 'Kim', 'Department': 'IoT', 'University': 'Soonchunhyang'}

# data.json의 이름으로 파일 생성
with open('data.json', 'w') as f:
    json.dump(dict_data, f)