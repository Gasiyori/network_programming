# 2개의 IoT 디바이스 정보로부터 데이터 수집
# 디바이스1

import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 7777)) # 디바이스1 바인딩
sock.listen()
user, addr = sock.accept() # 디바이스 1 연결
# print("client_1 connect success") # 디버깅용

print("Connect with client")

while True:
    msg = int(user.recv(1024).decode())

    if msg == 1: # 정상 수신인 경우
        print("int 1")
        temp = random.randint(1, 50)
        humid = 0
        illum = 0
        # 영어로 illuminance인데 과제 내용은 Iilum이라 되어있음.

        msg = f"Temp={temp}, Humid={humid}, Illum={illum}"
        
        user.send(msg.encode())
    
    elif msg == 2: # 정상 수신인 경우
        temp = 0
        humid = random.randint(1, 100) #습도 랜덤 정수
        illum = 0
        # 영어로 illuminance인데 과제 내용은 Iilum이라 되어있음.

        msg = f"Temp={temp}, Humid={humid}, Illum={illum}"
        
        user.send(msg.encode())
    
    elif msg == 3: # 정상 수신인 경우
        temp = 0
        humid = 0
        illum = random.randint(1, 150) #조도 랜덤 정수
        # 영어로 illuminance인데 과제 내용은 Iilum이라 되어있음.

        msg = f"Temp={temp}, Humid={humid}, Illum={illum}"
        
        user.send(msg.encode())