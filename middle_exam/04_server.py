# 30%의 데이터 손실 발생 가정, 70%만 응답 전송

from socket import *
import random

BUFF_SIZE = 1024
port = 5555

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    sock.settimeout(None) # 소켓의 블로킹모드 타임아웃 설정
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.randint(1, 10) <= 5: # 50% 확률로 데이터 손실 가정
            continue # 수신하지 않고 무시
        else: # 정상적 데이터 수신 가정
            sock.sendto(b'pong', addr)  # pong 전송
            print('<-', data.decode()) # 보낸 메시지 표기
            break