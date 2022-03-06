#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        int tribonacciEfficient(int n) {
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

        int tribonacciMemoization(int n) {

            vector<int> dp(n+1);

            dp[1] = 1;
            dp[2] = 1;

            return helper(n, dp);
        }

        int helper(int n, vector<int>& memo) {

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

        int tribonacciDynamicProgramming(int n) {

            if (n == 0) {
                return 0;
            } else if ( 1 <= n && n <= 2 ) {
                return 1;
            }

            vector<int> dp(n+1);

            dp[1] = 1;
            dp[2] = 1;

            for(int i = 3; i <= n; i++ ) {
                dp[i] = dp[i-3] + dp[i-2] + dp[i-1];
            }

            return dp[n];
        }
};


int main() {

    int n = 4;

    Solution solution;
    cout <<  solution.tribonacciEfficient(n) << endl;
    cout <<  solution.tribonacciMemoization(n) << endl;
    cout <<  solution.tribonacciDynamicProgramming(n) << endl;

    return 0;
}