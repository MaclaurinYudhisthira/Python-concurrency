'''

    This code is written for python 3.8
    
    Results are returned by executer.map() in sequence each process was started.

    If an exception occers in a process then the exception will be rasied while the result is returned by the executor.

    Whenever we use a context manager all the process in the scope of context manager will join the main process before end of the context manager automatically. 

'''
import concurrent.futures
import time

start = time.perf_counter()

def do_somthing(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1 ]
    results = executor.map(do_somthing, secs)

    # Here results are returned by executer.map() in sequence each process was started
    for result in results:
        print(result)

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")