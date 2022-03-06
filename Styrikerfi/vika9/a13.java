import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;

public class a13 extends Thread {
    Semaphore toilet;
    Semaphore breakfast;
    Semaphore food;
    Semaphore drinks;
    Semaphore driveToSchool;
    Semaphore clearTable;
    String name;
    public a13(String nafn, Semaphore toil, Semaphore breakfast, Semaphore food, 
        Semaphore drink, Semaphore drive, Semaphore table){
        this.name = nafn;
        this.toilet = toil;
        this.food = food;
        this.drinks = drink;
        this.driveToSchool = drive;
        this.clearTable = table;
        this.breakfast = breakfast;
    }

	@Override
	public void run(){
        if(name == "child"){
            try {
                toilet.acquire();
                useToilet(this.name);
                toilet.release();
                
                breakfast.acquire(2);
                haveBreakfast(this.name);
                driveToSchool.release(3);
                //System.out.println("end of child");
            } catch (InterruptedException e) {
                System.out.println(e);
            }

        }
        else if(name == "mother"){
            try {
                toilet.acquire();
                useToilet(this.name);
                toilet.release();
    
                drinks.acquire();
                prepareFood(this.name);
                System.out.println("Breakfast is ready!");
                
                breakfast.release(4);
                driveToSchool.acquire(4);
                takeAndDriveToSchool(this.name);
                //System.out.println("end of mother");

            } catch (InterruptedException e) {
                System.out.println(e);
            }

        }
        else if(name == "father"){
            try {
                toilet.acquire();
                useToilet(this.name);
                toilet.release();
    
                prepareDrink(this.name);
                drinks.release();
                driveToSchool.acquire(2);
                clearTable(this.name);

                //System.out.println("end of father");
            } catch (InterruptedException e) {
                System.out.println(e);
            }

        }
    }
	
    public static void main(String[] args) {
        Semaphore toilet = new Semaphore(1);
        Semaphore food = new Semaphore(0);
        Semaphore drinks = new Semaphore(0);
        Semaphore breakfast = new Semaphore(0);
        Semaphore drive = new Semaphore(0);
        Semaphore table = new Semaphore(1);

        a13 child1 = new a13("child", toilet, breakfast, food, drinks, drive, table);
        a13 child2 = new a13("child", toilet, breakfast, food, drinks, drive, table);
        a13 father = new a13("father", toilet, breakfast, food, drinks, drive, table);
        a13 mother = new a13("mother", toilet, breakfast, food, drinks, drive, table);
        child2.start(); child1.start(); father.start(); mother.start();

        //System.out.println("in thread: " + Thread.currentThread().getName());
        try {
            child1.join(); child2.join(); father.join(); mother.join();
            
        } catch (InterruptedException e) {
            System.out.println(e);
        }
    }

    public void useToilet(String threadName){
        System.out.println(threadName + " is using the toilet!");
        // try {
        //     TimeUnit.SECONDS.sleep(1);
        // } catch (InterruptedException e) {
        //     System.out.println(e);
        // }
    }
    public void prepareFood(String threadName){
        System.out.println(threadName + " is preparing food!");
        // try {
        //     TimeUnit.SECONDS.sleep(1);
        // } catch (InterruptedException e) {
        //     System.out.println(e);
        // }
    }
    public void prepareDrink(String threadName){
        System.out.println(threadName + " is preparing drinks!");
        // try {
        //     TimeUnit.SECONDS.sleep(1);
        // } catch (InterruptedException e) {
        //     System.out.println(e);
        // }
    }
    public void haveBreakfast(String threadName){
        System.out.println(threadName + " is having breakfast!");
        // try {
        //     TimeUnit.SECONDS.sleep(1);
        // } catch (InterruptedException e) {
        //     System.out.println(e);
        // }
        
    }
    public void takeAndDriveToSchool(String threadName){
        System.out.println(threadName + " is taking and driving the children to school!");
        // try {
        //     TimeUnit.SECONDS.sleep(1);
        // } catch (InterruptedException e) {
        //     System.out.println(e);
        // }
    }
    public void clearTable(String threadName){
        System.out.println(threadName + " is clearing the table!");
        // try {
        //     TimeUnit.SECONDS.sleep(1);
        // } catch (InterruptedException e) {
        //     System.out.println(e);
        // }
    }
}