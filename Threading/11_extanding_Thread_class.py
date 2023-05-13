'''

    This code is written for python version 3.8

    Code source/credit: https://superfastpython.com/extend-thread-class/

''' 
# SuperFastPython.com
# example of extending the Thread class and return values
from time import sleep
from threading import Thread
 
# custom thread class
class CustomThread(Thread):
    # override the run function
    def run(self):
        # block for a moment
        sleep(1)
        # display a message
        print('This is coming from another thread')
        # store return value
        self.value = 99
 
# create the thread
thread = CustomThread()
# start the thread
thread.start()
# wait for the thread to finish
print('Waiting for the thread to finish')
thread.join()
# get the value returned from run
value = thread.value
print(f'Got: {value}')