from socket import *
import threading

port = 3333
BUFFSIZE = 1024

def recvTask(sock):
    while True:
        data = sock.recv(BUFFSIZE)
        print(data.decode())

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', port))

th = threading.Thread(target=recvTask, args=(sock,))
th.daemon = True
th.start()

my_id = input('ID를 입력하세요: ')
sock.send(('[' + my_id + ']').encode())

while True:
    msg = '[' + my_id + '] ' + input()
    sock.send(msg.encode())