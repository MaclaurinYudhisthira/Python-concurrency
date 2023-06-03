'''

    This code is written for python 3.8
    
    Source: https://youtu.be/sp7EhjLkFY4

'''
import multiprocessing

def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n)

if __name__ == "__main__":
    numbers = [2,3,5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())