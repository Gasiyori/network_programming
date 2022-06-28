# TCP 통신을 통한 서버-클라이언트간 계산기 프로그램
# 클라이언트 부분

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

while True:
    msg = input("Enter a formula for calculation with space : ")

    if msg == 'q': # q 입력시 종료
        break
    else: # 그 외(수식 등)의 경우
        try:
            sock.send(msg.encode()) # 인코딩해서 전송
        except: # 오류 발생 예외처리
            print("Error!")
            break
    
    print(sock.recv(1024).decode()) # 디코딩해서 결과 출력
