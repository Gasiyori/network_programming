import socket

port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

mbox_index = {} # mboxID 목록 딕셔너리 생성

while True:    
    msg, addr = sock.recvfrom(BUFFSIZE)

    if msg.decode() == "quit": # 수신해서 디코딩
        break

    command, mboxID, *message = msg.decode().split() # 명령(send, receive), mboxID, message로 스플릿. #message에는 문자열 저장    
    message = " ".join(message) # 패킹된 문자열 합쳐서 문자열로 만듬

    if command == 'send': # send 수신한 경우
        if mboxID not in mbox_index: # mboxID 목록에 딕셔너리 key가 존재하지 않으면
            mbox_index[mboxID] = [] # 리스트를 키값으로 갖는 딕셔너리 생성
        
        # 존재하면 키 값에 추가    
        mbox_index[mboxID].append(message)

        # OK 메시지 전송
        sock.sendto("OK".encode(), addr) #인코딩해서 전송
        
    elif command == 'receive': # receive 수신한 경우 데이터 전송
        #mbox_index에 mboxID가 존재하지 않거나, mbox_index가 비어있는 경우
        if (mboxID not in mbox_index) or (not bool(mbox_index[mboxID])):
            sock.sendto("No messages".encode(), addr) # 인코딩해서 전송
        else: #존재하는 경우
            sock.sendto(mbox_index[mboxID].pop(0).encode(), addr) # 가장 앞의 문자 꺼내서 전송

sock.close()