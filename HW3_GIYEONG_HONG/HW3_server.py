# TCP 통신을 통한 서버-클라이언트간 계산기 프로그램
# 서버

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000)) # 바인딩
s.listen(2) # 동시 2개까지 소켓 연결 가능
client, addr = s.accept()

while True:
    msg = client.recv(1024).decode()
    
    num1, op, num2 = msg.split()

    num1, num2 = int(num1), int(num2)

    if op == '+':
        result = num1 + num2
        result = str(result)
    elif op == '-':
        result = num1 - num2
        result = str(result)
    elif op == '*':
        result = num1 * num2
        result = str(result)
    elif op == '/': # round 활용하여 소수점 1자리까지 반올림처리
        result = round((num1 / num2), 1)
        result = str(result)
    else:
        result = "Operand is wrong!"
    
    client.send(result.encode())