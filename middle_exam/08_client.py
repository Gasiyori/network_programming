import socket

address = ("localhost", 3333)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Enter a message:\"send mboxId message\" or \"receive mboxId\" : ")
    if msg == 'quit': # 전송 후 종료
        s.send(msg.encode())
        break

    else:
        s.send(msg.encode()) #send a message to server
        data = s.recv(BUFSIZE) #receive message from server
    
    print(data.decode())
    
s.close()