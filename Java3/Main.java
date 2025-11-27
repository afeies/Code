package Java3;

public class Main {
    public static void main(String[] args) {
        // define the task
        // anonymous class: define the class and create an instance in one step
        Runnable task = new Runnable() {
            @Override
            public void run() {
                for (int i = 1; i <= 5; i++) {
                    System.out.println("Count: " + i);
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        };

        // java.lang.Thread can execute a task in a thread

        public class Thread {
            // constructor
            // takes a Runnable object (which contains a run() method)
            // stores it internally
            // when you call start(), the Thread will execute that Runnable's run() method in a new thread
            public Thread(Runnable task);

            public void start() // creates a new thread, calls run()
            public void join() // waits for this thread to finish

            public void sleep(long millis) // pauses the thread
            public void interrupt() // requests the thread to stop
        }

        // create thread with the task
        Thread thread = new Thread(task);
        thread.start();
        System.out.println("Main thread continues...");
    }
}

// public interface Runnable {
//     public abstract void run();
// }

class MyTask implements Runnable {
    @Override
    public void run() {
        // this code exeutes in the new thread
        System.out.println("Hello from thread: " + Thread)
        // do some work
    }
}

Thread thread = new Thread(new myTask());
thread.start(); // this launches the new thread, which calls run()