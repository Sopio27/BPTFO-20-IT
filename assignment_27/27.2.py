# დავალება 2.

# დაწერეთ ასინქრონული ფუნქცია, რომელიც რენდომად არჩეული დროით დააყოვნებს და დაბეჭდავს რიცხვებს 1-დან 10-მდე

import asyncio
import random

async def delay_print(number, time):
    print(f"number {number} is being delayed for {time} seconds")
    await asyncio.sleep(time)
    print(f"number {number} is finished")
    print(f"result: {number}")

async def main():
    
    tasks= []

    for i in range(3):
        delay = random.randint(1,5)
        tasks.append(delay_print(i,delay))
    
    all_tasks = asyncio.gather(*tasks)
    await all_tasks


asyncio.run(main())
