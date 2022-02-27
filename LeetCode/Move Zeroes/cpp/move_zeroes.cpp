#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:

        void moveZeroes(vector<int>& nums) {

            // Count the zeroes
            int numZeroes = 0;
            for (size_t i = 0; i < nums.size(); i++) {
                numZeroes += (nums[i] == 0);
            }

            // Make all the non-zero elements retain their original order.
            vector<int> ans;
            for (size_t i = 0; i < nums.size(); i++) {
                if (nums[i] != 0) {
                    ans.push_back(nums[i]);
                }
            }

            // Move all zeroes to the end
            while (numZeroes--) {
                ans.push_back(0);
            }

            // Combine the result
            for (size_t i = 0; i < nums.size(); i++) {
                nums[i] = ans[i];
            }
        }

        void moveZeroesSpaceOptimal(vector<int>& nums) {
            int lastNonZeroFoundAt = 0;
            // If the current element is not 0, then we need to
            // append it just in front of last non 0 element we found. 
            for (size_t i = 0; i < nums.size(); i++) {
                if (nums[i] != 0) {
                    nums[lastNonZeroFoundAt++] = nums[i];
                }
            }
            // After we have finished processing new elements,
            // all the non-zero elements are already at beginning of array.
            // We just need to fill remaining array with 0's.
            for (size_t i = lastNonZeroFoundAt; i < nums.size(); i++) {
                nums[i] = 0;
            }
        }

    void moveZeroesOptimal(vector<int>& nums) {
        for (size_t lastNonZeroFoundAt = 0, cur = 0; cur < nums.size(); cur++) {
            if (nums[cur] != 0) {
                swap(nums[lastNonZeroFoundAt++], nums[cur]);
            }
    }
}

};


int main() {

    vector<int> nums = {0,1,0,3,12};

    Solution solution;
    solution.moveZeroesSpaceOptimal(nums);

    for(const auto ele: nums) {
        cout << ele << " ";
    }

    return 0;
}