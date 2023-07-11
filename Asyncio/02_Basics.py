'''
    
    This code is written for python version 3.8

    Source: https://youtu.be/6RbJYN7SoRs

'''

import asyncio

async def main():
    task = asyncio.create_task(other_fucntion())
    print("A")
    await asyncio.sleep(5)
    print("B")
    return_value = await task
    print(f"Return value was: {return_value}")

async def other_fucntion():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return 10

asyncio.run(main())