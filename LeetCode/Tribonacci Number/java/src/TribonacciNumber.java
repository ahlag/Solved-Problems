public class TribonacciNumber {

    public static int tribonacciEfficient(int n) {
        if (n < 3) return n == 0 ? 0 : 1;

        int tmp, x = 0, y = 1, z = 1;
        for(int i = 3; i <= n; i++) {
            tmp = x + y + z;
            x = y;
            y = z;
            z = tmp;
        }

        return z;
    }

    public static int tribonacciMemoization(int n) {

        int[] dp = new int[n+1];

        dp[1] = 1;
        dp[2] = 1;

        return helper(n, dp);
    }

    public static int helper(int n, int[] memo) {

        if (n == 0) {
            return 0;
        } else if ( memo[n] != 0 ) {
            return memo[n];
        }

        if (memo[n] == 0) {
            memo[n] = helper(n - 1, memo) + helper(n - 2, memo) + helper(n - 3, memo);
        }

        return memo[n];

    }


    public static int tribonacciDynamicProgramming(int n) {

        if (n == 0) {
            return 0;
        } else if ( 1 <= n && n <= 2 ) {
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
        System.out.println(tribonacciMemoization(4));
        System.out.println(tribonacciEfficient(4));
    }

}
