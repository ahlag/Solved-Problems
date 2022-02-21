#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        vector<int> sortedSquaresTwoPointers(vector<int>& nums) {
            int n = nums.size();

            vector<int> result(n);

            int left = 0;
            int right = n - 1;

            for (int i = n - 1; i >= 0; i--) {
                int square;
                if (abs(nums[left]) < abs(nums[right])) {
                    square = nums[right];
                    right--;
                } else {
                    square = nums[left];
                    left++;
                }
                result[i] = square * square;
            }
            return result;
        }

        vector<int> sortedSquaresArray(vector<int>& nums) {
            
            int n = nums.size();
            vector<int> res(n);
            for(size_t i = 0; i < nums.size(); i++) res[i] = nums[i] * nums[i];
            sort(res.begin(), res.end());
            return res;
    }
};


int main() {

    vector<int> nums = {-4,-1,0,3,10};

    Solution solution;

    vector<int> res1 = solution.sortedSquaresArray(nums);

    for(const auto &value: res1) {
        cout << value << ' ';
    }

    cout << endl;
    
    vector<int> res2 = solution.sortedSquaresTwoPointers(nums);
    
    for(const auto &value: res2) {
        cout << value << ' ';
    }

    return 0;
}