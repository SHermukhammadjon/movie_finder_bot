import asyncio

async def main1():
    # print('hello')
    await asyncio.sleep(2)
    print('world1')
    
async def main2():
    # print('hello')
    await asyncio.sleep(1)
    print('world2')
    
asyncio.run(main1())
asyncio.run(main2())