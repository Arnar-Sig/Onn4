public class scheduler {
    public void emulatedScheduler(){

        // Time slice of current process expired
        if (called by timer interrupt) { 
            pcb = running;
            addToTail(pcb, ready);
            running = removeFromHead(ready);
            interruptsOn();
            switchTo(running);
        } 
        // I/O request by current process
        else if (called by I/O system call) {
            pbc = running;
            addToTail(pcb, waiting);
            running = removeFromHead(ready);
            if (running == null){
                sleep()
            }
            else{
                interruptsOn();
                switchTo(running);
            }
        } 
        // I/O of process ioCompleted completed
        else if (called by I/O interrupt) {
             pcb = findAndRemove(isCompleted);
             addToTail(pcb, ready);
             pcb = running;
             interruptsOn();
             switchTo(running);
        }
        // Further code outside if statements (if required)
    }




















  public static void main(String[] args){
      System.out.println("main");
    }
}