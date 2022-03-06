public class TribonacciNumber {


    public static int tribonacciDynamicProgramming(int n) {

        if (n == 0) {
            return 0;
        } else if ( 1 <= n && n <= 2 ) {
            System.out.println(11111);
            return 1;
        }

        int[] dp = new int[n+1];

        dp[1] = 1;
        dp[2] = 1;

        for(int i = 3; i <= n; i++ ) {
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1];
        }

        return dp[n];
    }

    public static void main(String[] args) {

        int n = 4;

        System.out.println(tribonacciDynamicProgramming(n));
//        System.out.println(containsDuplicateHashSet(nums));
    }

}
