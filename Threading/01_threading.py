'''

    This code is written for python version 3.8

    List of modules available for concurrent execution in python: https://docs.python.org/3/library/concurrency.html

    Thread: https://en.wikipedia.org/wiki/Thread_(computing)
    
    Threading sholud be used for IO bound tasks.

    Applications of multithreading:
    1. Video game: player is running and shooting at the same time there is a different thread for each action
    2. Multimedia Graphics: streaming app like OBS showing videos from different cameras
    3. Animations
    4. Web server: number of requests are processed at the same time
    5. Applications (to reduce execution time)

    Youtube Videos:
    https://www.youtube.com/watch?v=GqHLztqy0PU
    https://www.youtube.com/watch?v=IEEhzQoKtQU
    https://www.youtube.com/playlist?list=PLI4OVrCFuY57b_16D8xs7-hmABHncVD_w


'''

import threading
import time

start = time.perf_counter()

def do_somthing():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

# Synchronous execution
# do_somthing()
# do_somthing() 

# Creating threads
t1 = threading.Thread(target = do_somthing)
t2 = threading.Thread(target = do_somthing)

# Starting the execution of  threads
t1.start()
t2.start()

# The main thread will wait for threads to join and other thread will keep on executing
# If .join() is not called thread will join the main thread naturally when its execution is done
t1.join()
t2.join()

finish = time.perf_counter() 
print(f'Finished in {round(finish-start, 2)} seconds(s)')