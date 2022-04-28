import java.util.concurrent.locks.Condition;

// You are free to modify this class, e.g. add fields, methods,
// constructors, extend from class Thread etc. with these two exceptions:
// 1. Do not change the name of this class nor put it into another package
// 2. Do not modify the name and input and output parameter of the main method.

public class MyAssignment16 {
	int counter;

	public MyAssignment16(){
		counter = 0;
	}
	public synchronized void inc(){
		counter++;
	}
	public void signal(){
		notify();
	}
	public void semWait(){
		try {
			this.wait();
		} catch (Exception e) {
			System.out.println(e);
		}
	}

	public static long main(long iterationsPerThread) {
		MyAssignment16 mon = new MyAssignment16();
		Thradur nr1 = new Thradur(0, mon, iterationsPerThread);
		Thradur nr2 = new Thradur(1, mon, iterationsPerThread);
		nr1.start(); nr2.start();

		try {
			nr1.join(); nr2.join();
		} catch (Exception e) {
			System.out.println(e);
		}
		System.out.println();
		return mon.counter;
	}
}
