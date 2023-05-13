'''

    This code is written for python version 3.8

    https://en.wikipedia.org/wiki/Race_condition
    
'''

from threading import *

class Bus:
    def __init__(self, name, available_seats ):
        self.name = name
        self.available_seats = available_seats

    def reserve(self, seats_req):
        print(f"Welcome to {self.name}")
        print(f"Available seats are: {self.available_seats}")
        if self.available_seats >= seats_req:
            nm = current_thread().name
            print(f"{seats_req} are allocated to {nm}")
            self.available_seats -= seats_req
        else:
            print("Sorry! seats are not available.")

b1 = Bus("Mahalakshmi Bus Service", 2)

t1 = Thread(target = b1.reserve, args = (1,), name = 'Jay')
t2 = Thread(target = b1.reserve, args = (2,), name = 'Raj')

t1.start()
t2.start()