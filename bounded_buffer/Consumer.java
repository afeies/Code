package bounded_buffer;

public class Consumer implements Runnable {
    private final BoundedBuffer<Integer> buffer;

    public Consumer(BoundedBuffer<Integer> buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            while (true) {
                int val = buffer.take();
                System.out.println("Consumed: " + val);
                Thread.sleep(150); // slow down for visibility
            }
        } catch (InterruptedException e ) {
            Thread.currentThread().interrupt();
        }
    }
}
