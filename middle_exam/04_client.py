from socket import *
import random
import time

BUFF_SIZE = 1024
port = 5555

sock = socket(AF_INET, SOCK_DGRAM)
sock.connect(('localhost', port))

msg = 'ping'
reTx = 0

while reTx <= 2: # 2번까지 재전송
    resp = str(reTx) + ' ' + msg
    sock.send(resp.encode())

    send_time = time.time() # 송신 시간 기록

    sock.settimeout(2) # 소켓의 timeout 설정. 해당 timeout 내 메시지
    # 수신을 못하면 timeout 예외 발생
    try:
        data, addr = sock.recvfrom(BUFF_SIZE)
        break #t 수신하면 즉시 브레이크
    except timeout:
        reTx += 1
        continue
    else:
        break

if reTx == 3:
    print("Fail") # 재전송 횟수가 3회 이상 초과일 때.
    exit()

print(data.decode())

if data.decode() == 'pong':
    recv_time = time.time()
    rtt = recv_time - send_time

    print(f"Success (RTT: {rtt})")