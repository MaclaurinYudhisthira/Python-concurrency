'''

    This code is written for python version 3.8

    Rlock can be acquired and released multiple times where normal lock cannot be.

    https://www.geeksforgeeks.org/python-difference-between-lock-and-rlock-objects/

'''

from threading import *

class Bus:
    def __init__(self, name, available_seats, rlock):
        self.name = name
        self.available_seats = available_seats
        self.rlock=rlock

    def reserve(self, seats_req):
        print(f"Welcome to {self.name}")
        self.rlock.acquire()
        print(f"Available seats are: {self.available_seats}")
        if self.available_seats >= seats_req:
            nm = current_thread().name
            print(f"{seats_req} are allocated to {nm}")
            self.available_seats -= seats_req
        else:
            print("Sorry! seats are not available.")
        self.rlock.release()

b1 = Bus("Mahalakshmi Bus Service", 2, RLock())

t1 = Thread(target = b1.reserve, args = (1,), name = 'Jay')
t2 = Thread(target = b1.reserve, args = (2,), name = 'Raj')

t1.start()
t2.start()