import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;

public class a13 {
    public static void main(String[] args) {
        Semaphore toilet = new Semaphore(1);
        Semaphore breakfast = new Semaphore(2);

        Thread child1 = new Thread();
        Thread child2 = new Thread();
        Thread father = new Thread();
        Thread mother = new Thread();
        
        child1.run();
        child2.run();
        father.run();
        mother.run();
        System.out.println("HEY!");
        System.out.println("in thread: " + Thread.currentThread().getName());
        try {
            Thread.currentThread().join();
        } catch (InterruptedException e) {
            System.out.println(e);
        }
        System.out.println("should not be here :(");
    }
    
    





    public void useToilet(String threadName){
        System.out.println(threadName + " is using the toilet!");
        try {
            TimeUnit.SECONDS.sleep(1);
        } catch (InterruptedException e) {
            System.out.println(e);
        }
    }
    public void prepareFood(String threadName){
        System.out.println(threadName + " is preparing food!");
        try {
            TimeUnit.SECONDS.sleep(1);
        } catch (InterruptedException e) {
            System.out.println(e);
        }
    }
    public void prepareDrink(String threadName){
        System.out.println(threadName + " is preparing drinks!");
        try {
            TimeUnit.SECONDS.sleep(1);
        } catch (InterruptedException e) {
            System.out.println(e);
        }
    }
    public void haveBreakfast(String threadName){
        System.out.println(threadName + " is having breakfast!");
        try {
            TimeUnit.SECONDS.sleep(1);
        } catch (InterruptedException e) {
            System.out.println(e);
        }
        
    }
    public void takeAndDriveToSchool(String threadName){
        System.out.println(threadName + " is taking and driving the children to school!");
        try {
            TimeUnit.SECONDS.sleep(1);
        } catch (InterruptedException e) {
            System.out.println(e);
        }
    }
    public void clearTable(String threadName){
        System.out.println(threadName + " is clearing the table!");
        try {
            TimeUnit.SECONDS.sleep(1);
        } catch (InterruptedException e) {
            System.out.println(e);
        }
    }
}



