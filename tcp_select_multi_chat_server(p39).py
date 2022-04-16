import socket, select
import time

socks = [] # 소켓 리스트
BUFFER = 1024
PORT = 3333

s_sock = socket.socket() # TCP 소켓
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock) # 소켓 리스트에 서버 소켓을 추가
# print(str(PORT) + '에서 접속 대기 중')
print('Server Started')

while True:
    # 읽기 이벤트(연결요청 및 데이터수신) 대기
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    for s in r_sock: # 수신(읽기 가능한) 소켓 리스트 검사

        if s == s_sock: # 새로운 클라이언트의 연결 요청 이벤트 발생
            c_sock, addr = s_sock.accept()
            socks.append(c_sock) # 연결된 클라이언트 소켓을 소켓 리스트에 추가
            print('new client', addr)
        
        else: # 기존 클라이언트의 데이터 수신 이벤트 발생
            msg = s.recv(BUFFER).decode() # 메시지를 수신했을 때
            if not msg: # 메시지가 비었으면
                s.close()
                socks.remove(s) # 연결 종료된 클라이언트 소켓을 소켓 리스트에서 제거
                continue
            elif 'quit' in msg:
                print(addr, 'exited')
            
            print(time.asctime() + ' ' + str(s)[-21:-2] + ':' + msg)

            for x in socks:
                if x != socks[0] and x != s:
                    x.send(msg.encode())