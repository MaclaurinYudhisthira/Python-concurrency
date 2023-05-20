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
    return f'Done Sleeping...{seconds}'
'''

    Observing beahviour of as_completed() by giving different times
    it returns the futures as and when the threads complete their execution 
    in earlier and some of the later programs we are getting results when every single thread is done executing 

'''
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    futures = [executor.submit(do_somthing, sec) for sec in secs]

    for f in concurrent.futures.as_completed(futures):
        print(f.result())

finish = time.perf_counter() 
print(f'Finished in {round(finish-start, 2)} seconds(s)')