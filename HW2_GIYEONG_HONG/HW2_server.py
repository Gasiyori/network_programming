# 서버-클라이언트간 문자열(이름), 정수(학번) 전송
# 서버

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000)) # 바인딩
s.listen(2) # 동시 2개까지 소켓 연결 가능

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode()) # 클라이언트에 접속 확인 메시지 보냄

# 학생 이름 수신 후 출력
    print(client.recv(1024).decode())

# 학생 학번 전송
    client.send((20171520).to_bytes(4, 'big'))

    client.close()