import java.util.Scanner;

public class Soultion1003 {
    static int count_zero = 0;
    static int count_one = 0;
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int i = 0 ; i < t ; i++){
            int n = sc.nextInt();
            count_zero = 0;
            count_one  = 0;
            fibo(n);
            System.out.println(Integer.toString(count_zero)+" "+Integer.toString(count_one));
        }
        sc.close();
        return;
    }
    public static long fibo(long n){
        if( n == 0 ){
            count_zero++;
            return 0;
        }
        if( n == 1 ){
            count_one++;
            return 1;
        }
        return fibo(n-2)+fibo(n-1);
    }
}
