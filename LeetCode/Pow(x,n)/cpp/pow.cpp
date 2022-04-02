#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    double fastPowRecursive(double x, long long n) {
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

    double myPow(double x, int n) {
        long long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        return fastPowRecursive(x, N);
    }

    double myPowIterative(double x, int n) {
        long long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        double ans = 1;
        double current_product = x;
        for (long long i = N; i ; i /= 2) {
            if ((i % 2) == 1) {
                ans = ans * current_product;
            }
            current_product = current_product * current_product;
        }
        return ans;
    }

};


int main() {

    Solution solution;

    double x = 2;
    int n = 10;

    cout << solution.myPowIterative(x, n) << endl;

    return 0;
}