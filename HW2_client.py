# 서버-클라이언트간 문자열(이름), 정수(학번) 전송
# 클라이언트

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024) # 1024바이트

print(msg.decode())

# 본인 이름 문자열로 전송
sock.send(b"Giyeong Hong")

# 본인 학번 수신 후 출력
print(int.from_bytes(sock.recv(1024), 'big'))