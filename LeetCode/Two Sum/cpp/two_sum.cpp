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

        vector<int> twoSumMap(vector<int>& nums, int& target) {
            vector<int> result;
                unordered_map<int,int> seen;
                int size = nums.size();
                for(int i=0; i < size; i++) {
                    int complement = target-nums[i];
                    if( seen.find(complement) != seen.end()) {
                        result.push_back(seen[complement]);
                        result.push_back(i);
                        break;
                    }
                    seen[nums[i]]=i;
                    // seen.insert({nums[i], i});
                }
            return result;
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