'''

    This code is written for python version 3.8

'''

import threading
import time

e = threading.Event()

lines=None

def read():
    global lines
    n=1
    while True:
        if not e.is_set():
            with open('read.txt','r') as fp:
                print("Reading from file A")        
                try:    
                    lines = fp.readlines()[n-1:n+4]
                    n=n+5
                except:
                    lines = fp.readlines()[n:]
                    print("Here")
                    e.clear()
                    return
            time.sleep(.2)
            e.set()
            print(n)
        
        

def write():
    e.wait()
    while e.is_set():
        with open('write.txt','a') as fp:
            print("Writing to file B")
            fp.writelines(lines)
        e.clear()
        time.sleep(.2)
        e.wait()

t1 = threading.Thread(target=read)
t2 = threading.Thread(target=write)

t1.start()
t2.start()


# with open('read.txt','w') as fp:
#     fp.writelines([f"Line {i}\n" for i in range(1,53)])