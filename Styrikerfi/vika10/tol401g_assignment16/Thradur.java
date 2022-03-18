
public class Thradur extends Thread {
    int id;
    long iterations;
    MyAssignment16 monitor;

    public Thradur(int curr, MyAssignment16 mon, long iters){
        id = curr;
        monitor = mon;
        iterations = iters;
    }

    @Override
    public void run(){
        int i = 0;
        while(i < iterations){
            System.out.print(id);
            monitor.inc();
            i++;
        }

    }
	public static long main() {
        return 0;
	}
}
