import java.io.*;
import java.util.StringTokenizer;
import java.util.Scanner;


public class tildesJAVA {
    public static int[] items;
    public static int[] sizes;

    public static int myFind(int p){
        while(items[p] != p){
            items[p] = items[items[p]];
            p = items[p];
        }
        return p;
    }
    public static void myUnion(int p,int q){
        int p_root = myFind(p);
        int q_root = myFind(q);
        if(p_root != q_root){
            if (sizes[p_root] < sizes[q_root]){
                int temp = p_root;
                p_root = q_root;
                q_root = temp;
            }
            items[q_root] = p_root;
            sizes[p_root] = sizes[p_root] + sizes[q_root];
        }
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int q = scan.nextInt();
        items = new int[n];
        sizes= new int[n];
        for(int i=0; i<n; i++){
            items[i] = i;
            sizes[i] = 1;
        }
        for(int i=0; i<q; i++){
            String stafur = String.valueOf(scan.next().charAt(0));
            int fyrri = scan.nextInt();
            if(stafur.equals("t")){
                int seinni = scan.nextInt();
                myUnion(fyrri-1, seinni-1);
            }
            else{
                int rot = myFind(fyrri);
                System.out.println(rot);
            }
        }
    }
}