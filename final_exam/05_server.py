# 비동기방식(asyncio 사용)으로 1:1 채팅 구현하기

from socket import *
import ssl

port = 2500
BUFSIZE = 1024

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#서버 인증서와 개인키 설정
context.load_cert_chain(certfile='server.pem', keyfile='server.key')

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

ssl_sock = context.wrap_socket(sock, server_side=True)
ssl_conn, (remotehost, remoteport) = ssl_sock.accept()
print('connected by', remotehost, remoteport)

while True:
    data = ssl_conn.recv(BUFSIZE)
    print("Received message: ", data.decode())
    ssl_conn.send(data)

    msg = input("Message to send: ")
    ssl_conn.send(msg.encode())
    data = ssl_conn.recv(BUFSIZE)
    print("Received message: %s"%data.decode())