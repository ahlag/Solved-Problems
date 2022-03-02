#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:

        vector<vector<int>> threeSumTwoPointers(vector<int>& nums) {
            sort(begin(nums), end(nums));
            vector<vector<int>> res;
            for (int i = 0; i < nums.size() && nums[i] <= 0; ++i)
                if (i == 0 || nums[i - 1] != nums[i]) {
                    twoSumII(nums, i, res);
                }
            return res;
        }

        void twoSumII(vector<int>& nums, int i, vector<vector<int>> &res) {
            int lo = i + 1, hi = nums.size() - 1;
            while (lo < hi) {
                int sum = nums[i] + nums[lo] + nums[hi];
                if (sum < 0) {
                    ++lo;
                } else if (sum > 0) {
                    --hi;
                } else {
                    res.push_back({ nums[i], nums[lo++], nums[hi--] });
                    while (lo < hi && nums[lo] == nums[lo - 1])
                        ++lo;
                }
            }
        }

        vector<vector<int>> threeSumHashSet(vector<int>& nums) {
            sort(begin(nums), end(nums));
            vector<vector<int>> res;
            for (int i = 0; i < nums.size() && nums[i] <= 0; ++i)
                if (i == 0 || nums[i - 1] != nums[i]) {
                    twoSum(nums, i, res);
                }
            return res;
        }

        void twoSum(vector<int>& nums, int i, vector<vector<int>> &res) {
            unordered_set<int> seen;
            for (int j = i + 1; j < nums.size(); ++j) {
                int complement = -nums[i] - nums[j];
                if (seen.count(complement)) {
                    res.push_back({nums[i], complement, nums[j]});
                    while (j + 1 < nums.size() && nums[j] == nums[j + 1]) {
                        ++j;
                    }
                }
                seen.insert(nums[j]);
            }
        }

        vector<vector<int>> threeSumNoSort(vector<int>& nums) {
            set<vector<int>> res;
            unordered_set<int> dups;
            unordered_map<int, int> seen;
            for (int i = 0; i < nums.size(); ++i)
                if (dups.insert(nums[i]).second) {
                    for (int j = i + 1; j < nums.size(); ++j) {
                        int complement = -nums[i] - nums[j];
                        auto it = seen.find(complement);
                        if (it != end(seen) && it->second == i) {
                            vector<int> triplet = {nums[i], nums[j], complement};
                            sort(begin(triplet), end(triplet));
                            res.insert(triplet);
                        }
                        seen[nums[j]] = i;
                    }
                }
            return vector<vector<int>>(begin(res), end(res));
        }


};


int main() {

    vector<int> num = {-1,0,1,2,-1,-4};

    Solution solution;
    
    vector<vector<int>> res = solution.threeSumNoSort(num);

    for (int i = 0; i < res.size(); i++) {
        for (int j = 0; j < res[i].size(); j++) {
            cout << res[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}