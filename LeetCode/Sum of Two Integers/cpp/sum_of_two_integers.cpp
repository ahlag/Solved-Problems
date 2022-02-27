#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        int getSum(int x, int y) {

            while (y != 0) {
                unsigned carry = x & y;
                x = x ^ y;
                y = carry << 1;
            }
            
            return x;
        }
};


int main() {

    Solution solution;
    cout <<  solution.getSum(3, 5) << endl;
    cout <<  solution.getSum(3, -5) << endl;

    return 0;
}