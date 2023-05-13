'''

    This code is written for python version 3.8

    Thread communication can be done in 3 ways:
        
        1. Event object
        2. Condition object
        3. Queue module

    event object can establish communication between two objects only

'''


import threading
import time

e = threading.Event()

def task():
    print("Game is started")
    time.sleep(5)
    e.set()

def end():
    e.wait()
    if e.is_set():
        print("Code for destroying session")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=end)

t1.start()
t2.start()