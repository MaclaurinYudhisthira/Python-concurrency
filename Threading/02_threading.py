'''

    This code is written for python version 3.8

'''

import threading
import time

start = time.perf_counter()

def do_somthing():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

threads = []

for _ in range(10):
    t = threading.Thread(target=do_somthing)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter() 
print(f'Finished in {round(finish-start, 2)} seconds(s)')