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

## Source Tutorial:
https://youtu.be/fKl2JW_qrso