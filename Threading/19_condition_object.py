'''

    This code is written for python version 3.8

    condition object is used to esteblish communication between multiple thread

'''
import threading
import time

def write_data():
    con.acquire()
    with open('report.txt','w') as file1:
        days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for day in days:
            temp = input(f"Enter the temperature for {day}: ")
            file1.write(temp+"\n")
    con.notify_all()
    con.release()

def max_temp():
    con.acquire()
    with open('report.txt','r') as file1:
        data=file1.readlines()
        temp=[float(n.strip("\n")) for n in data]
        print("Maximum Temperature: ",max(temp))
        con.release()

def avg_temp():
    con.acquire()
    with open('report.txt','r') as file1:
        data=file1.readlines()
        temp=[float(n.strip("\n")) for n in data]
        print("Average Temperature: ",sum(temp)/len(temp))
        con.release()

con = threading.Condition()

t1 = threading.Thread(target=write_data)
t2 = threading.Thread(target=max_temp)
t3 = threading.Thread(target=avg_temp)

t1.start()
t2.start()
t3.start()