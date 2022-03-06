// You are free to modify this class, e.g. add fields, methods,
// constructors, extend from class Thread etc. with the two exceptions:
// 1. Do not change the name of this class nor put it into another package
// 2. Do not modify the name and input and output parameter of the main method.
import java.net.*;
import java.util.concurrent.Semaphore;
import java.io.*;

public class MyAssignment14 extends Thread{
	static volatile long result = 0;
	Semaphore guardian;
	int name;
	long iterations;
	public MyAssignment14(long iters, Semaphore guard, int nafn){
		iterations = iters;
		guardian = guard;
		name = nafn;
	}

	@Override
	public void run(){
		int i = 0;
		try {
			while(i < iterations){
				System.err.println(name);
				guardian.acquire();
				long curr = result;
				curr++;
				result = curr;
				i++;
				guardian.release();
			}

		} catch (Exception e) {
			System.out.println(e);
		}

	}

	public static long main(long iterationsPerThread){
		Semaphore guardian = new Semaphore(1);
		MyAssignment14 nr1 = new MyAssignment14(iterationsPerThread, guardian, 0);
		MyAssignment14 nr2 = new MyAssignment14(iterationsPerThread, guardian, 1);
		nr1.start();
		nr2.start();
		try{
				nr1.join();
		} 
		catch(InterruptedException e){
				System.out.println(e);
		}
		try{
			nr2.join();
		} 
		catch(InterruptedException e){
				System.out.println(e);
		}
		return result;
	}
}
