'''

    This code is written for python version 3.8

    Lock is a thread synchronization technique used to avoid race condtion.
    
    https://en.wikipedia.org/wiki/Lock_(computer_science)

    when a lock is acquired by a thread on critical section then no other thread can access (execute) that section of code until the lock is released

    https://youtu.be/MbZQ8Mz8xeM

'''

from threading import *

class Bus:
    def __init__(self, name, available_seats, lock):
        self.name = name
        self.available_seats = available_seats
        self.lock=lock

    def reserve(self, seats_req):
        print(f"Welcome to {self.name}")
        self.lock.acquire()
        print(f"Available seats are: {self.available_seats}")
        if self.available_seats >= seats_req:
            nm = current_thread().name
            print(f"{seats_req} are allocated to {nm}")
            self.available_seats -= seats_req
        else:
            print("Sorry! seats are not available.")
        self.lock.release()

b1 = Bus("Mahalakshmi Bus Service", 2, Lock())

t1 = Thread(target = b1.reserve, args = (1,), name = 'Jay')
t2 = Thread(target = b1.reserve, args = (2,), name = 'Raj')

t1.start()
t2.start()