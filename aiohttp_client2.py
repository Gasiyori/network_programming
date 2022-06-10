import aiohttp
import asyncio

async def main():
    async with aiohttp.request('GET', 'https://python.org/', connector=aiohttp.TCPConnector(ssl=False)) as rsp:
        print(rsp.status)
        print(rsp.headers)
        print(await rsp.text())

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())