'''

    This code is written for python 3.8

    pip install playsound
    sudo apt install libgirepository1.0-dev
    pip install pygobject


'''

import multiprocessing
from time import sleep
from playsound import playsound
 
# for playing note.wav file


def child():
    while True:
        print("Child process starts here.")
        sleep(2)
        with open('write.txt','a+') as fp:
            fp.write('DGH\n')
        sleep(2)
        with open('write.txt','a+') as fp:
            fp.write('DGH22\n')
        print("Child process ends here.")

if __name__ == "__main__":
    print("Main process starts here.")
    numbers = [2,3,5]

    # p = multiprocessing.Process(target=child)
    p = multiprocessing.Process(target=child, daemon=False)

    p.start()
    while True:
        sleep(1)
    # p.join()
    print("Main process ends here.")