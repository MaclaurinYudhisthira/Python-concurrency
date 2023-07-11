'''
    
    This code is written for python version 3.8

    Threading Pre-emptive multitasking uses Asyncio, on the other hand, uses cooperative multitasking.

    https://realpython.com/python-concurrency/
    https://en.wikipedia.org/wiki/Preemption_%28computing%29#Preemptive_multitasking
    https://en.wikipedia.org/wiki/Cooperative_multitasking


    Concurrency Type 	                    Switching Decision 	                                                    Number of Processors
    Pre-emptive multitasking (threading) 	The operating system decides when to switch tasks external to Python. 	1
    Cooperative multitasking (asyncio) 	    The tasks decide when to give up control. 	                            1
    Multiprocessing (multiprocessing) 	    The processes all run at the same time on different processors. 	    Many


    While getting somthing done asynchronously, we start the task and do not wait for the task to get complete instead we anitcipate(await) the completion of task and in the mean time focus on other tasks.

    Asynchronous programming is a technique that enables your program to start a potentially long-running task and still be able to be responsive to other events while that task runs, rather than having to wait until that task has finished.
    (https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Introducing) 

'''

import asyncio, requests
import argparse
import time

parser = argparse.ArgumentParser(prog='Asyncio Basics 01', description='Intro to asyncio', epilog='Comparing sync ans asyc version in terms of performance')
parser.add_argument('-a', '--async_', action='store_true')
parser.add_argument('-n','--num')
args = parser.parse_args()

n=10

def sync_fetch_some(n):
    res=requests.get(f'https://reqres.in/api/user{n}')
    res=requests.get(f'https://dog.ceo/api/breeds/image/random')
    
async def async_fetch_some(n):
    res=requests.get(f'https://reqres.in/api/user{n}')
    res=requests.get(f'https://dog.ceo/api/breeds/image/random')

async def async_main():
    await asyncio.gather(*[async_fetch_some(i+1) for i in range(n)])


if __name__ == "__main__":
    if args.num:
        n=int(args.num)
    print(f"n = {n}")
    if args.async_:
        print("Async version")
        s = time.perf_counter()
        asyncio.run(async_main())
        elapsed = time.perf_counter() - s
        print(f"Async version of {__file__} executed in {elapsed:0.2f} seconds.")
    else:
        print("Sync version")
        s = time.perf_counter()
        for i in range(n):
            sync_fetch_some(i+1)
        elapsed = time.perf_counter() - s
        print(f"Sync version of {__file__} executed in {elapsed:0.2f} seconds.")