#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        int findNumbers(vector<int>& nums) {
            
            int cnt = 0;

            for(auto num: nums) {

                int subcnt = 0;
                while(num > 0) {
                    num /= 10;
                    subcnt++;
                }
                if (subcnt % 2 == 0) cnt++;
            }

            return cnt;
        }
    
};


int main() {

    vector<int> nums = {12, 345, 2, 6, 7896};

    Solution solution;
    int res;

    res = solution.findNumbers(nums);

    cout << res << endl;

    return 0;
}