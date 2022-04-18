# 2개의 IoT 디바이스 정보로부터 데이터 수집
# 디바이스2

import socket
import random
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 2500))
# print("client_2 connect success") # 디버깅용

while True:
    msg = sock.recv(1024).decode()

    if msg == 'Register': # 정상 수신인 경우
        while True:
            htb = random.randint(40, 140) #심박 수 랜덤 정수
            stp = random.randint(2000, 6000) #걸음 수 랜덤 정수
            cal = random.randint(1000, 4000) #칼로리 랜덤 정수

            msg = f"Hearbeat={htb}, Steps={stp}, Cal={cal}"
            
            sock.send(msg.encode())

            time.sleep(5)
            
    # elif msg == 'quit': # 종료 메시지의 경우
    #     sock.close()
    #     break
    # else: # 그 외 값 (예외처리용)
    #     print("error!")