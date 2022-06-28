# 중간고사 문제와 유사하지만 aiohttp를 사용해 제작
# 뭔가 돌아는 가는데 뭔가 안됨. 아마 감점 받았을거고 aiohttp 조금 더 연습하면 알 수 있을 듯

from aiohttp import web
import aiofiles

def success_msg_header(mimeType):
    result = f"HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n" # f-string으로 병합하여 반환
    return result

async def proc_query(request):
    _, _, filename, _ = str(request).split() # 파싱
    filename = filename.strip("/") # '/' 제거, filename 추출 완료
    print(filename)

    if filename == "index.html":
        f = open(filename, 'r', encoding='utf-8')
        # mimeType = 'text/html'
        # c.send(success_msg_header(mimeType).encode()) # 성공 헤더 인코딩(함수 참고)
        # c.send(f.read().encode('euc-kr')) # 한글 텍스트 파일이라 인코딩 형식 지정해서 전송

        return web.Response(text=f.read(), content_type='text/html')

    elif filename == "iot.png":
        f = open(filename, 'rb') # rb = read binary, 이진 파일로 읽기
        # mimeType = 'image/png'
        # c.send(success_msg_header(mimeType).encode())
        # c.send(f.read()) #파일 읽어서 전송
        return web.Response(text=f.read().decode(), content_type='image/png')

    elif filename == "favicon.ico":
        f = open(filename, 'rb')
        return web.Response(text=str(f.read()), content_type='image/x-icon')

    else:
        return web.Response(text = "Not Found", content_type='text/html')

app = web.Application()
app.add_routes([web.get('/index.html', proc_query),
                web.get('/iot.png', proc_query),
                web.get('/favicon.ico', proc_query)])
                
web.run_app(app, port=8000)