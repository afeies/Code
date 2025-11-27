# Buffer
- buffer: temporary holding area where data waits before being processed. we need buffers because of asynchronous and unpredicatable mismatches.
    - producer add items and when buffer becomes full, there is no space left so producers block
    - consumer removes items so when buffer becomes empty, no items left so consumers block

# BoundedBuffer<T>
- a thread-safe buffer with fixed capacity
- producers call put(item)
    - must wait if buffer is full
    - wake up consumers when they add an item
- consumers call take()
    - must wait if buffer is empty
    - wake up producers when they remove an item

# Producer Thread
- adds numbers into the buffer
- implements Runnable: provides run() method to tell the thread what to execute
- this class is not the thread, it is the task the thread runs
    - Thread: the worker
    - Producer: the work the worker performs
    - run(): the instructions for the worker

# Consumer Thread
- reads numbers from the buffer

# Additional notes
- wait() in while loop to check before and after
- call notifyAll() rather than notify()
1. Producer implements Runnable
2. defines run(), which is the task
3. Thread thread = new Thread(new Producer(...))
4. Thread object created
5. thread.start()
6. new OS thread is launched
7. the OS thread calls Producer.run()
- wait() releases the lock and reacquires it on wake
- loops handle spurious wakeups and re-check conditions
- notifyAll() wakes all waiting threads, but they still must compete for the lock
- interrupting a waiting thread throws an InterruptedException
    - we interrupt a thread when we want it to stop waiting, stop what its doing, or shut down gracefully
- notify() can cause deadlock
- intrinsic monitor lock has only one holder
- spurious wakepus are caused by JVM internals
- locks ensure invariant + prevent race conditions
- calling wait() without the intrinsic lock throws IllegalMonitorStateException
- atomic types provide lock-free atomic operations
- LinkedBlockingQueue is a data-exchange (blocking) collection
- exectutor.shutdown() stops accepting new tasks, but allows existing tasks to finish normally
- !(numReaders != 0 && writeLocked)
    - you can't have readers and a writer simultaneously
- the OS, not the JVM, schedules threads