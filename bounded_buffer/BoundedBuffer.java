package bounded_buffer;

public class BoundedBuffer<T> {
    
    // T: type placeholder
    private final Object lock = this; // lock used for intrisic monitor
    private final T[] buffer;
    private int count = 0;            // how many items are in buffer
    private int head = 0;             // next take index
    private int tail = 0;             // next put index

    @SuppressWarnings("unchecked")
    public BoundedBuffer(int capacity) {
        buffer = (T[]) new Object[capacity];
    }

    // producer: adds an item
    // when count == buffer.length, the number of stored items equals capacity
    // the producer must wait because there is not room to add more
    // when it finally adds an item, it notifies others (consumer) becuase the buffer is no longer empty
    public void put(T item) throws InterruptedException {
        synchronized (lock) {
            // always wait in a loop
            while (count == buffer.length) {
                lock.wait(); // releases lock while waiting
            }

            // perform the write
            buffer[tail] = item;
            tail = (tail + 1) % buffer.length;
            count++;

            notifyAll(); // wake consumers who might be wwaiting for data
        }
    }

    // consumer: removes an item
    public T take() throws InterruptedException {
        synchronized (lock) {
            while (count == 0) {
                lock.wait();
            }

            // perform the read
            T item = buffer[head];
            head = (head + 1) % buffer.length;
            count--;

            lock.notifyAll();
            return item;
        }
    }
}
