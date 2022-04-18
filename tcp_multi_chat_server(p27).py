from socket import *
import threading
import time

port = 3333
BUFFSIZE = 1024

client_list = []

print('Server Started')

def recv_send(client, addr):
    while True:
        msg = client.recv(BUFFSIZE).decode() # 현재 클라이언트에서 수신 대기
        if 'quit' in msg: # quit인 경우
            if client in client_list: # 리스트에서 찾아서
                print(addr, 'exited') #종료 메시지 출력 후
                client_list.remove(client)
            client.close() # 뭔가 이상하긴 한데 if문 내부에 있어도 되고 여기 있어도 됨
            exit()

        print(time.asctime() + str(addr) + ':' + msg)

        for x in client_list: # 리스트를 순회하며
            if client != x: # 현재 클라이언트를 제외한
                x.send(msg.encode()) # 나머지 클라이언트에 메세지 전송

while True:
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)

    client, addr = s.accept()
    print('new client', addr)

    # 각 소켓에서 수신 및 송신 관리 스레드
    rs = threading.Thread(target=recv_send, args=(client, addr))
    rs.start()

    client_list.append(client)