#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        bool containsDuplicateHashSet(vector<int>& nums) {
            unordered_set<int>seen;
            for(size_t i = 0; i < nums.size(); i++) seen.insert(nums[i]);
            if (seen.size() != nums.size()) return true;
            return false;
        }

        bool containsDuplicateArray(vector<int>& nums) {
            sort(nums.begin(), nums.end());
            for(size_t i = 0; i < nums.size()-1; i++) if(nums[i] == nums[i+1]) return true;
            return false;
    }
};


int main() {

    vector<int> nums = {1,2,3,1};

    Solution solution;
    cout <<  solution.containsDuplicateArray(nums) << endl;
    cout <<  solution.containsDuplicateHashSet(nums) << endl;

    return 0;
}