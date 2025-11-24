package bounded_buffer;

public class Producer implements Runnable {
    private final BoundedBuffer<Integer> buffer;

    // dependency injection: producer needs buffer
    public Producer(BoundedBuffer<Integer> buffer){
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            for (int i = 0; i <= 20; i++) {
                buffer.put(i);
                System.out.println("Produced: " + i);
                Thread.sleep(100); // slow down for visibility
            }
        } catch (InterruptedException e) {
            // another thread is telling you to stop what you're doing
            Thread.currentThread().interrupt();
        }
    }
}
