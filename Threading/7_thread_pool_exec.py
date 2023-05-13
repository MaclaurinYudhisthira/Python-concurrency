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

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_somthing, secs)
    '''
    
        if an exception occurs in the thread then the exception will be raised 
        when we actually retrive the results from the itreator returned by executor.map()
        so we can handle the exception at that time 
    
    '''
    for result in results:
        print(result)

finish = time.perf_counter() 
print(f'Finished in {round(finish-start, 2)} seconds(s)') 