'''

    This code is written for python version 3.8
    thread pool executer is in concurrent.futures module

    A future or promise can be thought of as a value that will eventually become available.
    http://dist-prog-book.com/chapter/2/futures.html
    https://en.wikipedia.org/wiki/Futures_and_promises

'''

import concurrent.futures
import time

start = time.perf_counter()

def do_somthing(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

with concurrent.futures.ThreadPoolExecutor() as executor:
    future1 = executor.submit(do_somthing, 1.7)
    future2 = executor.submit(do_somthing, 1.7)

    print(future1.result())
    print(future2.result())

finish = time.perf_counter() 
print(f'Finished in {round(finish-start, 2)} seconds(s)')