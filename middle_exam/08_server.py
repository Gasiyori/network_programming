from re import S
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

mbox_index = {} # mboxID 목록 딕셔너리 생성

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

            command, mboxID, *message = msg.split() # 명령(send, receive), mboxID, message로 스플릿. #message에는 문자열 저장    

            print(command, mboxID, *message)

            if not msg or msg == 'quit': # 메시지가 비거나 quit이면
                s.close()
                socks.remove(s) # 연결 종료된 클라이언트 소켓을 소켓 리스트에서 제거
                continue

            elif command == 'send': # send 수신한 경우
                if mboxID not in mbox_index: # mboxID 목록에 딕셔너리 key가 존재하지 않으면
                    mbox_index[mboxID] = [] # 리스트를 키값으로 갖는 딕셔너리 생성
                
                # 존재하면 키 값에 추가    
                mbox_index[mboxID].append(message)

                # OK 메시지 전송
                s.send("OK".encode()) #인코딩해서 전송

            elif command == 'receive': # receive 수신한 경우 데이터 전송
                #mbox_index에 mboxID가 존재하지 않거나, mbox_index가 비어있는 경우
                if (mboxID not in mbox_index) or (not bool(mbox_index[mboxID])):
                    s.send("No messages".encode()) # 인코딩해서 전송
                else: #존재하는 경우
                    tmp = str(mbox_index[mboxID].pop(0))
                    s.send(tmp[2:-2].encode()) # 가장 앞의 문자 꺼내서 전송
                    # 리스트 형태로 나와서 필터링을 해줘야 하는데 시간이 없네...
                    # 됨
                    