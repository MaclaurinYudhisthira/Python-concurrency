'''

    This code is written for python version 3.8

'''

import threading
import time

e = threading.Event()

def read():
    line=10 
    while not e.is_set():
        
        if not line:
            print("EOF, nothing to read")
            e.clear()
            break

        print("Reading from file A")
        line-=5
        time.sleep(2)
        e.set()
        e.wait()
        
        
        

def write():
    e.wait()
    while e.is_set():
        print("Writing to file B")
        time.sleep(2)
        e.clear()
        if not e.is_set():
            break    
        e.wait()

t1 = threading.Thread(target=read)
t2 = threading.Thread(target=write)

t1.start()
t2.start()