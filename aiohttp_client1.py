import aiohttp
import asyncio

async def main():
    # async with aiohttp.ClientSession(connector =aiohttp.TCPConnector(verify_ssl= False)) as session: # 아래 방법 말고 이걸로도 가능
        # async with session.get('https://python.org') as rsp: # 오류 발생. ssl 비활성화 시 실행 가능
    async with aiohttp.ClientSession() as session:
        async with session.get('https://python.org', ssl=False) as rsp:
            print(rsp.status)
            print(rsp.headers)
            print(await rsp.text())

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())