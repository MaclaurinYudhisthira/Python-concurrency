'''

    This code is written for python version 3.8

    if exception occers in one thread it won't affect tther threads

    https://youtu.be/rmxjR79NhbE

'''
import threading
from time import sleep

def custom_hook(args):
    print("Exception occurred in thread")
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

def display():
    for i in range(4):
        sleep(0.1)
        print("Hello:" + 10)

def show():
    for i in range(4):
        print("Hello")
        sleep(0.5)

# Execute code by commenting/uncommenting the next line
# threading.excepthook = custom_hook

t1 = threading.Thread(target=display)
t2 = threading.Thread(target=show)

t1.start()
t2.start()

t1.join()
t2.join()

for i in range(4):
    print("Bye")