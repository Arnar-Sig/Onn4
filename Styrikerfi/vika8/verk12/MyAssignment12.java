// You are free to modify this class, e.g. add fields, methods,
// constructors, extend from class Thread etc. with the two exceptions:
// 1. Do not change the name of this class nor put it into another package
// 2. Do not modify the name and input and output parameter of the main method.
import java.net.*;
import java.io.*;

public class MyAssignment12 extends Thread{
	static volatile long result = 0;
	static boolean flag[] = new boolean[2];
	static int turn;
	long iterations;
	int currID;
	
	public MyAssignment12(long iters, int id){
		iterations = iters;
		currID = id;
	}

	@Override
	public void run(){
		flag[currID] = true;
		int otherID = Math.abs(1-currID);
		turn = otherID;
		while(flag[otherID] == true && turn == otherID){
			// Waiting
		}
		
		int i = 0;
		while(i < iterations){
			long curr = result;
			curr++;
			result = curr;
			i++;
		}
		flag[currID] = false;
	}
	public static long main(long iterationsPerThread){
		MyAssignment12 nr1 = new MyAssignment12(iterationsPerThread, 0);
		MyAssignment12 nr2 = new MyAssignment12(iterationsPerThread, 1);
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

