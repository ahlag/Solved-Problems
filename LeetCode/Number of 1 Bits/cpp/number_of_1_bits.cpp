#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:

    int hammingWeightIterate(uint32_t n) {
        int cnt=0;  // count of set bit
        while(n>0){  // iterate until all bits are traversed
            if((n&1)>0) // check the parity of first bit from right
                ++cnt;
            n=n>>1; //n=n/2, shift one bit to right
        }
        return cnt;
    }

        int hammingWeightBitManipulation(uint32_t n) {
            int count = 0;
            
            while (n) {
                n &= (n - 1);
                count++;
            }
            
            return count;
        }

};

int main() {

    int num = 11;

    Solution solution;
    
    cout << solution.hammingWeightBitManipulation(num) << endl;

    return 0;
}