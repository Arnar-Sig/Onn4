// You are free to modify this class, e.g. add fields, methods,
// constructors, extend from class Thread etc. with the two exceptions:
// 1. Do not change the name of this class nor put it into another package
// 2. Do not modify the name and input and output parameter of the main method.
import java.net.*;
import java.io.*;

public class MyAssignment11 extends Thread{
	static volatile long result = 0;
	long iterations;
	public MyAssignment11(long iters){
		iterations = iters;
	}

	@Override
	public void run(){
		int i = 0;
		while(i < iterations){
			long curr = result;
			curr++;
			result = curr;
			i++;
		}
	}
	public static long main(long iterationsPerThread){
		MyAssignment11 nr1 = new MyAssignment11(iterationsPerThread);
		MyAssignment11 nr2 = new MyAssignment11(iterationsPerThread);
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

