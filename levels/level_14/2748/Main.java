import java.util.*;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        if( n <= 0 ){
            System.out.println(0); 
            return;
        } 
        if( n == 1 || n == 2){
            System.out.println(1); 
            return;
        } 
        
        long[] pool = new long[91]; 
        pool[0] = 0;
        pool[1] = 1;
        pool[2] = 1;

        for(int i = 3; i <= n;i++){
            pool[i] = pool[i-1] + pool[i-2];
        }
        System.out.println(pool[n]);
        return;
    }
}
