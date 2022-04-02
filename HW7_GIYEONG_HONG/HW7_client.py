from socket import *
import random

BUFF_SIZE = 1024
port = 5555

sock = socket(AF_INET, SOCK_DGRAM)
sock.connect(('localhost', port))

while True:
    msg = input('-> ')
    reTx = 0

    while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        sock.send(resp.encode())
        sock.settimeout(2) # 소켓의 timeout 설정. 해당 timeout 내 메시지
        # 수신을 못하면 timeout 예외 발생
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break
    
    sock.settimeout(None) # 소켓의 블로킹모드 타임아웃 설정
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.randint(1, 10) <= 5: # 50% 확률로 데이터 손실 가정
            continue # 수신하지 않고 무시
        else: # 정상적 데이터 수신 가정
            sock.sendto(b'ack', addr)  # ack 전송
            print('<-', data.decode()) # 보낸 메시지 표기
            break