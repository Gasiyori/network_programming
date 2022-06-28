# 메일함 구현 / 클라이언트

import socket

port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input("Enter a message:\"send mboxId message\" or \"receive mboxId\" : ")
    if msg == 'quit': # 전송 후 종료
        sock.sendto(msg.encode(), ('localhost', port))    
        break
    else: # quit이 아니면 정상 동작
        sock.sendto(msg.encode(), ('localhost', port)) #메시지 서버로 보냄

        msg, addr = sock.recvfrom(BUFFSIZE) #msg 변수 재활용, 메시지 수신
        print(msg.decode())

sock.close()