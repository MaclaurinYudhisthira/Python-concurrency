'''

    This code is written for python version 3.8

    https://youtu.be/03Cs2rnCcWs

    start(): to start a thread
    run(): to resume a blocked/sleeping thread

'''

import threading

print(threading.current_thread())
print(threading.current_thread().name)
print(threading.current_thread().ident)
print(threading.current_thread().is_alive())