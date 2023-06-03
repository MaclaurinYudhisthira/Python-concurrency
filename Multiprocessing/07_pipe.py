'''

    This code is written for python 3.8

    Source: https://youtu.be/y88wGWRsWcE
    
    https://superfastpython.com/multiprocessing-pipe-in-python/

'''

from multiprocessing import Process, Pipe
from time import sleep

def shared(child_conn):
    child_conn.send("Hello")
    sleep(5)
    print("Child process end here.")

perent_conn, child_conn = Pipe()

p = Process(target=shared, args=(child_conn,))
p.start()

print(perent_conn.recv())
print("Perent process end here.")