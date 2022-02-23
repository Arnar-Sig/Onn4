import edu.princeton.cs.algs4.*;
public class Cookie<Key extends Comparable<Key>> {
  private MaxPQ<Key> lo;
  private MinPQ<Key> hi;
  private Key median;
  private int size;
  public void MedianFinder() {
    lo = new MaxPQ<Key>();
    hi = new MinPQ<Key>();
    median = null;
    size = 0;
  }
  public Key findMedian() {
    return median;
  }
  public Key deleteMedian() {
    size--;
    Key tmp = median;
    if(lo.size() > hi.size()){
      median = lo.delMax();
    }
    else if(!hi.isEmpty()){
      median = hi.delMin();
    }
    else{
      median = null;
    }
    return tmp;
  }
  public void insert(Key key) {
    size++;
    if(median == null){
      median = key;
      return;
    }
    if(key.compareTo(median) >= 0) {
      hi.insert(key);
      if(lo.size() < hi.size()){
        lo.insert(median);
        median = hi.delMin();
      }
    }
    else{
      lo.insert(key);
      if(lo.size() > hi.size() + 1){
        hi.insert(median);
        median = lo.delMax();
      }
    }
    return;
  }

  public static void main(String[] args){
    System.out.println("hi");
  }
}