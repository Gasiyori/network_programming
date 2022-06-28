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