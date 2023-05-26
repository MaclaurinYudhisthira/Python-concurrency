'''

    This code is written for python 3.8

    The args passed to a process has to be serializable using pickel

'''
import concurrent.futures
import time

start = time.perf_counter()

def do_somthing(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    return 'Done Sleeping'

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(do_somthing, 1) for _ in range(10)]
    
    for future in concurrent.futures.as_completed(results):
        print(future.result())

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")