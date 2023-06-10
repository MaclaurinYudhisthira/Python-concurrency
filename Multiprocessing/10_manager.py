'''

    This code is written for python 3.8

    Managers provide a way to create data which can be shared between different processes, including sharing over a network between processes running on different machines. A manager object controls a server process which manages shared objects. Other processes can access the shared objects by using proxies. 
    https://docs.python.org/3/library/multiprocessing.html#managers

    https://youtu.be/tKdolYuydVE

'''
from multiprocessing import Process, Manager, current_process

def worker(list1, num):
    list1.append(num)
    print(f"List accessed by {current_process().name}: {list1}")


mgr = Manager()
list1 = mgr.list()

p1 = Process(name='worker1', target=worker, args=(list1, 10))
p2 = Process(name='worker2', target=worker, args=(list1, 20))

p1.start()
p2.start()

p1.join()
p2.join()

print("Final list", list1)