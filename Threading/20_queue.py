'''

    This code is written for python version 3.8

    https://youtu.be/qLXG4V5fKzw

'''
from time import sleep
from threading import Thread
from queue import Queue

def producer(myque):
    print("Producer Start")
    n = int(input("Enter number of student"))
    for i in range(n):
        marks = float(input("Enter marks: "))
        myque.put(marks)
        sleep(1)
    myque.put(None)
    print("Producer End")

def consumer(myque):
    print("Consumer Start")
    while True:
        item = myque.get()
        if not item:
            break
        print(f"Got marks: {item}")
    print("Consumer End")

myque = Queue()

t1 = Thread(target = producer, args=(myque,))
t2 = Thread(target = consumer, args=(myque,))

t1.start()
t2.start()