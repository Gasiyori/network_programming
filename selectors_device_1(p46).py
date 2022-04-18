# 2개의 IoT 디바이스 정보로부터 데이터 수집
# 디바이스1

import socket
import random
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 2500))
# print("client_1 connect success") # 디버깅용

while True:
    msg = sock.recv(1024).decode()

    if msg == 'Register': # 정상 수신인 경우
        while True:
            temp = random.randint(0, 40) #온도 랜덤 정수
            humid = random.randint(0, 100) #습도 랜덤 정수
            illum = random.randint(70, 150) #조도 랜덤 정수
            # 영어로 illuminance인데 과제 내용은 Iilum이라 되어있음.

            msg = f"Temp={temp}, Humid={humid}, Illum={illum}"
            
            sock.send(msg.encode())

            time.sleep(3) # 3초마다 전송
            
    # elif msg == 'quit': # 종료 메시지의 경우
    #     sock.close()
    #     break
    # else: # 그 외 값 (예외처리용)
    #     print("error!")