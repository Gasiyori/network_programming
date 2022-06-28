# 2개의 IoT 디바이스 정보로부터 데이터 수집
# 사용자

import socket
import time # 시간을 위한 모듈

sock_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr_1 = ('localhost', 7777)
sock_1.connect(addr_1)
# print("addr_1 connect success") # 디버깅용

print("Connect with server")

while True:
    enter = input()
    sock_1.send(enter.encode()) # 1, 2, 3중에 입력해서 보냄
    data = sock_1.recv(1024).decode()
    print(data)

sock_1.close()