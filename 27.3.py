import asyncio

async def checkEven(number):
    if number % 2 == 0:
        return True
    return False

async def Square(number):
    number = number**2
    return number

async def main():
    user_input = int(input("Enter value:"))

    task1, task2 = await asyncio.gather(checkEven(user_input), Square(user_input))

    value1 = task1
    value2 = task2
    if value1:
        print(value2)

asyncio.run(main())
    

