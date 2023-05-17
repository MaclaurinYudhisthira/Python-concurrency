'''
    
    This code is written for python version 3.8

    Threading Pre-emptive multitasking uses Asyncio, on the other hand, uses cooperative multitasking.

    https://realpython.com/python-concurrency/
    https://en.wikipedia.org/wiki/Preemption_%28computing%29#Preemptive_multitasking
    https://en.wikipedia.org/wiki/Cooperative_multitasking


    Concurrency Type 	                    Switching Decision 	                                                    Number of Processors
    Pre-emptive multitasking (threading) 	The operating system decides when to switch tasks external to Python. 	1
    Cooperative multitasking (asyncio) 	    The tasks decide when to give up control. 	                            1
    Multiprocessing (multiprocessing) 	    The processes all run at the same time on different processors. 	    Many
    
'''