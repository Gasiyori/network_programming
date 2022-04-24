import selectors
import socket
import time

sel = selectors.DefaultSelector() # 이벤트 처리기(셀렉터) 생성

socket_list = []

def accept(sock, mask): # 새로운 클라이언트로부터 연결을 처리하는 함수
    conn, addr = sock.accept()
    print('connected from', addr)
    sel.register(conn, selectors.EVENT_READ, read) # 클라이언트 소켓 수신을 이벤트 처리기에 등록
    socket_list.append(conn)
    
def read(conn, mask): # 기존 클라이언트로부터 수신한 데이터를 처리하는 함수
    data = conn.recv(1024).decode()
    if not data:
        sel.unregister(conn) # 소켓 연결 종료 시, 이벤트 처리기에서 등록 해제
        conn.close()
        return

    for x in socket_list: # 리스트를 순회하며
        if conn != x: # 현재 클라이언트를 제외한
            x.send(data.encode()) # 나머지 클라이언트에 메세지 전송
    # 수신값 출력
    # 소켓 리스트??


sock = socket.socket()
sock.bind(('', 2500))
sock.listen(5)

# 서버 소켓(신규 클라이언트 연결을 처리하는 소켓)을 이벤트 처리기에 등록
# 즉, 새로운 연결 요청이 오면 accept 함수를 실행함
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select() # 등록된 객체에 대한 이벤트 감시 시작
    for key, mask in events: # 발생한 이벤트를 모두 검사
        callback = key.data # key.data: 이벤트 처리기에 등록한 callback 함수
        callback(key.fileobj, mask) # callback 함수 호출