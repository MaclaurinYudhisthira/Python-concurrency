'''

    This code is written for python version 3.8

    Semaphore can be used to limit the access to the shared resources with limited capacity.

    https://en.wikipedia.org/wiki/Semaphore_(programming) Read the Library analogy also

    Semaphore being counter based lock allows muliple acquire and realese 
    however the number of acquire() calls and realese() calls has to be equal 
    otherwise an exception may occure.

    To avoide this exception BoundedSemaphore() can be used this class handles this exception

'''

from threading import *
import time

sema_obj = Semaphore(3) # at max 3 threads can acquire the lock
# sema_obj = BoundedSemaphore(3)

def display(name):
    print(f"In display function {name}")
    
    sema_obj.acquire()
    print(f"Lock acquired by {name}")

    for i in range(5):
        print(f"Hello {name}")
        time.sleep(4)
    
    sema_obj.release()

    print(f"Realesed by {name}")

t1 = Thread(target = display, args = ('Thread-1',))
t2 = Thread(target = display, args = ('Thread-2',))
t3 = Thread(target = display, args = ('Thread-3',))
t4 = Thread(target = display, args = ('Thread-4',))
t5 = Thread(target = display, args = ('Thread-5',))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()