# 중간고사 문제와 거의 유사. asyncio 사용해서 구현
# big endian을 고려해야했는데 자료를 가지고 있지 않아서 구현 못했음.
# 여기서도 감점 먹었을 것으로 추정

import asyncio
import random

async def handle_asyncclient(reader, writer):
    print('client :', writer.get_extra_info('peername'))
    while True:
        data = await reader.read(12)
        if data == b'1':
            temp = random.randint(1, 50)
            humid = 0
            illum = 0
            msg = f"Temp={temp}, Humid={humid}, Illum={illum}"
            writer.write(msg.encode())
            await writer.drain()
            print(msg)
        elif data == b'2':
            temp = 0
            humid = random.randint(1, 100)
            illum = 0
            msg = f"Temp={temp}, Humid={humid}, Illum={illum}"
            writer.write(msg.encode())
            await writer.drain()
            print(msg)
        elif data == b'3':
            temp = 0
            humid = 0
            illum = random.randint(1, 150)
            msg = f"Temp={temp}, Humid={humid}, Illum={illum}"
            writer.write(msg.encode())
            await writer.drain()
            print(msg)
        elif len(data) == 0:
            break

    writer.close()
    await writer.wait_closed()
    print('connection was closed')

async def server_asyncmain():
    server = await asyncio.start_server(handle_asyncclient,'localhost', 7777)
    print('server started')
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(server_asyncmain())