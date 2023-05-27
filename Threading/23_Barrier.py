'''

    This code is written for python version 3.8
    
    A barrier is a synchronization primitive.
    It allows multiple threads to wait on the same barrier object instance (e.g. at the same point in code) until a predefined fixed number of threads arrive (e.g. the barrier is full), after which all threads are then notified and released to continue their execution. (source:https://superfastpython.com/thread-barrier-in-python/)

    https://youtu.be/3Y6l76AS4l4
    https://docs.python.org/3/library/threading.html#barrier-objects
    https://superfastpython.com/thread-barrier-in-python/

'''
import time
from threading import Barrier, Thread

b = Barrier(2)

def wait_on_barrier(name, time_to_sleep):
    for i in range(10):
        print(name," Running")
        time.sleep(time_to_sleep)
        print(name, " is waiting on barrier")
        b.wait()
    print(name, " is finished")

red = Thread(target= wait_on_barrier, args=["Red", 4])
blue = Thread(target= wait_on_barrier, args=["Blue", 5])

red.start()
blue.start()

time.sleep(15)
print("Aborting barrier")
b.abort()

# one other operation: reset()