'''

    This code is written for python version 3.8

'''

import threading
import time

e = threading.Event()

def light_switch():
    while True:
        print("Light is green")
        e.set()
        time.sleep(3)
        e.clear()
        print("Light is red")
        time.sleep(3)
        

def message():
    e.wait()
    while e.is_set():
        print("You can go!")
        time.sleep(.3)
        
        while not e.is_set():
            print("Please stop!")
            time.sleep(.3)
        
        e.wait()

t1 = threading.Thread(target=light_switch)
t2 = threading.Thread(target=message)

t1.start()
t2.start()