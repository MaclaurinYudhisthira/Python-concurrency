# Threading

List of modules available for concurrent execution in python: https://docs.python.org/3/library/concurrency.html

Thread: https://en.wikipedia.org/wiki/Thread_(computing)

Threading sholud be used for IO bound tasks.

Applications of multithreading:
1. Video game: player is running and shooting at the same time there is a different thread for each action
2. Multimedia Graphics: streaming app like OBS showing videos from different cameras
3. Animations
4. Web server: number of requests are processed at the same time
5. Applications (to reduce execution time)


### Thread pool executer
thread pool executer is in concurrent.futures module

A future or promise can be thought of as a value that will eventually become available.

http://dist-prog-book.com/chapter/2/futures.html

https://en.wikipedia.org/wiki/Futures_and_promises

### Lock
Lock is a thread synchronization technique used to avoid race condtion.

https://en.wikipedia.org/wiki/Lock_(computer_science)

when a lock is acquired by a thread on critical section then no other thread can access (execute) that section of code until the lock is released

https://youtu.be/MbZQ8Mz8xeM

### RLock
Rlock can be acquired and released multiple times where normal lock cannot be.

https://www.geeksforgeeks.org/python-difference-between-lock-and-rlock-objects/

### Semaphore
Semaphore can be used to limit the access to the shared resources with limited capacity.

https://en.wikipedia.org/wiki/Semaphore_(programming) Read the Library analogy to understand better.

Semaphore being counter based lock allows muliple acquire and realese however the number of acquire() calls and realese() calls has to be equal otherwise an exception may occure.

To avoide this exception BoundedSemaphore() can be used this class handles this exception

### Exception in threads
if exception occers in one thread it won't affect tther threads

https://youtu.be/rmxjR79NhbE

### Thread communication
Thread communication can be done in 3 ways:
        
1. Event object
2. Condition object: condition object is used to esteblish communication between multiple thread
3. Queue module

event object can establish communication between two objects only

### Resources
Youtube Videos:
* https://www.youtube.com/watch?v=GqHLztqy0PU
* https://www.youtube.com/watch?v=IEEhzQoKtQU
* https://www.youtube.com/playlist?list=PLI4OVrCFuY57b_16D8xs7-hmABHncVD_w

Docs:
* https://docs.python.org/3/library/concurrency.html
* http://dist-prog-book.com/chapter/2/futures.html
* https://en.wikipedia.org/wiki/Futures_and_promises
* https://en.wikipedia.org/wiki/Thread_(computing)
* https://superfastpython.com/extend-thread-class/
* https://en.wikipedia.org/wiki/Race_condition
* https://en.wikipedia.org/wiki/Lock_(computer_science)
* https://www.geeksforgeeks.org/python-difference-between-lock-and-rlock-objects/
* https://en.wikipedia.org/wiki/Semaphore_(programming) 