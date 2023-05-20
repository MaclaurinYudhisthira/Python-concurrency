'''

    This code is written for python version 3.8

'''
from time import sleep
from threading import Thread, Event
from queue import Queue

e = Event()
e.set()

def producer(myque):
    n=1
    while True:
        with open('read.txt','r') as fp:
            print("Reading from file A")
            # try:    
            lines = fp.readlines()[n-1:n+4]
            if lines==[]:
                print("End of file A. No more lines to read")
                myque.put(None)
                e.clear()
                break   
            myque.put(lines)
            n=n+5
            sleep(1)  
    

def consumer(myque):
    while e.is_set():
        lines = myque.get()
        if not lines:
            break
        with open('write.txt','a') as fp:
            print("Writing to file B")
            fp.writelines(lines)
        

myque = Queue()

t1 = Thread(target = producer, args=(myque,))
t2 = Thread(target = consumer, args=(myque,))

t1.start()
t2.start()