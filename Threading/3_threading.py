'''

    This code is written for python version 3.8
 
'''

import threading
import time

start = time.perf_counter()

def do_somthing(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')

threads = []

for _ in range(10):
    t = threading.Thread(target=do_somthing, args=(2,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter() 
print(f'Finished in {round(finish-start, 2)} seconds(s)')