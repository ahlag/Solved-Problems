public class Solution {

    private static double fastPowRecursive(double x, long n) {
        if (n == 0) {
            return 1.0;
        }
        double half = fastPowRecursive(x, n / 2);
        if (n % 2 == 0) {
            return half * half;
        } else {
            return half * half * x;
        }
    }
    public double myPow(double x, int n) {
        long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }

        return fastPowRecursive(x, N);
    }

    public static double myPowIterative(double x, int n) {
        long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        double ans = 1;
        double current_product = x;
        for (long i = N; i > 0; i /= 2) {
            if ((i % 2) == 1) {
                ans = ans * current_product;
            }
            current_product = current_product * current_product;
        }
        return ans;
    }

    public static void main(String[] args) {

        double x = 2.0;
        int v = 10;

        System.out.println(myPowIterative(x,v));

    }

}
