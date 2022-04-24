# 간단한 웹 서버 프로그램

from socket import *
import threading

s = socket() # 소켓 열고
s.bind(('', 8080)) # 바인딩
s.listen(10) # 10개 연결까지 허용

def success_msg_header(mimeType):
    result = f"HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n" # f-string으로 병합하여 반환
    return result

def multi_thread(c, filename):
    if filename == "index.html":
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html'
        c.send(success_msg_header(mimeType).encode()) # 성공 헤더 인코딩(함수 참고)
        c.send(f.read().encode('euc-kr')) # 한글 텍스트 파일이라 인코딩 형식 지정해서 전송
    elif filename == "iot.png":
        f = open(filename, 'rb') # rb = read binary, 이진 파일로 읽기
        mimeType = 'image/png'
        c.send(success_msg_header(mimeType).encode())
        c.send(f.read()) #파일 읽어서 전송
    elif filename == "favicon.ico":
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'
        c.send(success_msg_header(mimeType).encode())
        c.send(f.read()) #파일 읽어서 전송
    else:
        c.send(b"HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>")

while True:
    c, addr = s.accept() # 클라이언트, 주소저장

    data = c.recv(1024) # 데이터 수신
    msg = data.decode() # 파싱해서 디코딩
    req = msg.split('\r\n') # CR, NL으로 스플릿

    # req 내부에 스플릿 된 값들이 문자열의 리스트로 존재하므로 배열로 접근 가능
    # 첫 번째(인덱스 0) 값이 GET / index.html HTTP/1.1의 형식을 가짐
    # 따라서 이 값을 파싱하면 index.html을 얻을 수 있음

    get, filename, version = req[0].split() # 파싱
    filename = filename.strip("/") # '/' 제거, filename 추출 완료

    rs = threading.Thread(target=multi_thread, args=(c, filename))
    rs.start()

c.close()