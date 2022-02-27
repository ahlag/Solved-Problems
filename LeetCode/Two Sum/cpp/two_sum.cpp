#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int& target) {
            unordered_map<int, size_t>seen;

            for(int i = 0; i < nums.size(); i++) {
                
                if( seen.count((target - nums[i])) ) {
                    return {seen[target - nums[i]], i};
                } else {
                    seen[nums[i]] = i;
                }
            } 
            
        }

};


int main() {

    vector<int> nums = {2,7,11,15};
    int target = 9;

    Solution solution;
    vector<int> res = solution.twoSum(nums, target);

    for(const auto ele: res) {
        cout << ele << " ";
    }

    return 0;
}