#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:

        int climbStairs(int n) {
            if (n <= 2) return n;
            int prev = 2, prev2 = 1, res;
            for (int i = 3; i <= n; i++) {
                res = prev + prev2;
                prev2 = prev;
                prev = res;
            }
            return res;
        }

        int mk(int n,vector<int> &memo) {     
            if(n<0) return 0;
            if(memo[n]!=-1) return memo[n];
            if(n==0) return 1;
            return memo[n]=mk(n-1,memo)+mk(n-2,memo);
        }

    int climbStairsMem(int n) {
        vector<int> memo(n+1,-1);
        return mk(n,memo);
    }

    int climbStairsDP(int n) {
	    if(n<1) return 0;
        int a[100];
        a[0]=1;
        a[1]=2;
        for(int i=2;i<n;i++)
            a[i]=a[i-1]+a[i-2];
        return a[n-1];
    }

};


int main() {

    int n = 10;

    Solution solution;
    
    cout << solution.climbStairs(n) << endl;

    return 0;
}