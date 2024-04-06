import asyncio

async def think():
    print('Currently thinking')
    await asyncio.sleep(5)
    print('Finished thinking')

async def write():
    for i in range(2):
        print('Currently writing')
        await asyncio.sleep(2)
    print('Finished writing')

async def main():
    task1 = asyncio.create_task(think())
    task2 = asyncio.create_task(write())

    await task1
    await task2

asyncio.run(main())
