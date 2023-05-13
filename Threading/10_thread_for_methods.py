'''

    This code is written for python version 3.8

'''

import threading

# Creating thread for methods
# try for @classmethod and @staticmethod
class Example:
    def display(self,n):
        print(threading.current_thread())
        for i in range(n): 
            print('Hello world')

    @classmethod
    def display1(self,n):
        print(threading.current_thread())
        for i in range(n): 
            print('Hello world')
    
    @staticmethod
    def display2(n):
        print(threading.current_thread())
        for i in range(n): 
            print('Hello world')
    

e1 = Example()
t1 = threading.Thread(target=e1.display, args=(5,)) #self is passed automatically
t2 = threading.Thread(target=Example.display1, args=(5,)) 
t3 = threading.Thread(target=Example.display1, args=(5,)) 
t1.start()
t2.start()
t3.start()
for i in range(5):
    print("Welcome")