'''

    This code is written for python 3.8

    https://youtu.be/fKl2JW_qrso

    The args passed to a process has to be serializable using pickel

'''
import multiprocessing
import time

start = time.perf_counter()

def do_somthing(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print('Done Sleeping')

processes = []

for _ in range(10):
    p = multiprocessing.Process(target=do_somthing, args=[1.5,]) 
    processes.append(p)
    p.start()

for process in processes:
    process.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")