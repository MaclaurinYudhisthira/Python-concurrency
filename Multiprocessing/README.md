# Multiprocessing

The args passed to a process has to be serializable using pickel.

## executer.map()

Results are returned by executer.map() in sequence each process was started.

If an exception occers in a process then the exception will be rasied while the result is returned by the executor.

Whenever we use a context manager all the process in the scope of context manager will join the main process before end of the context manager automatically. 

## multiprocessing pool vs processpoolexecutor
Both are implemnetation of Pool (https://en.wikipedia.org/wiki/Pool_(computer_science))

Comperison of both is given here:

https://superfastpython.com/multiprocessing-pool-vs-processpoolexecutor/

## Inter process commutication
1. Queue (https://www.youtube.com/watch?v=sp7EhjLkFY4)
2. Pipe (https://superfastpython.com/multiprocessing-pipe-in-python/)iab
3. Shared variable (Array and value) (https://youtu.be/uWbSc84he2Q)
4. Manger (https://www.youtube.com/watch?v=tKdolYuydVE)
5. Socket
6. Rest API
7. File IO
8. DB IO

## Source Tutorial:
https://youtu.be/fKl2JW_qrso
https://docs.python.org/3/library/multiprocessing.shared_memory.html