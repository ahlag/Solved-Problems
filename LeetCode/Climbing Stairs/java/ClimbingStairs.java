public class ClimbingStairs {

    public int climbStairsRecursion(int n) {
        return climbStairsRecursionHelper(0, n);
    }
    public int climbStairsRecursionHelper(int i, int n) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        return climbStairsRecursionHelper(i + 1, n) + climbStairsRecursionHelper(i + 2, n);
    }

    public int climbStairsMemoization(int n) {
        int memo[] = new int[n + 1];
        return climbStairsMemoizationHelper(0, n, memo);
    }
    public int climbStairsMemoizationHelper(int i, int n, int memo[]) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        if (memo[i] > 0) {
            return memo[i];
        }
        memo[i] = climbStairsMemoizationHelper(i + 1, n, memo) + climbStairsMemoizationHelper(i + 2, n, memo);
        return memo[i];
    }

    public int climbStairsDP(int n) {
        if (n == 1) {
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    public int climbStairsFib(int n) {
        if (n == 1) {
            return 1;
        }
        int first = 1;
        int second = 2;
        for (int i = 3; i <= n; i++) {
            int third = first + second;
            first = second;
            second = third;
        }
        return second;
    }

    public static int climbStairsFibFormula(int n) {
        double sqrt5=Math.sqrt(5);
        double fibn=Math.pow((1+sqrt5)/2,n+1)-Math.pow((1-sqrt5)/2,n+1);
        return (int)(fibn/sqrt5);
    }

    public static void main(String[] args) {
        int n = 10;
        System.out.println(climbStairsFibFormula(10));
    }
}
