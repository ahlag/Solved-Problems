#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        int rec(vector<int>& nums,int idx){
            if(idx>=nums.size())return 0;
            return max(nums[idx]+rec(nums,idx+2),rec(nums,idx+1));
        }

        int robRecursion(vector<int>& nums) {
            return rec(nums,0);
        }

        int recMemo(vector<int>& nums,int idx,vector<int>&dp){
            if(idx >= nums.size()) return 0;
            if(dp[idx] != -1) return dp[idx];
            return dp[idx] = max(recMemo(nums, idx+1, dp), nums[idx] + recMemo(nums, idx+2, dp));
        }

        int robMemo(vector<int>& nums) {
            vector<int>dp(nums.size()+1,-1);
            return recMemo(nums,0,dp);
        }

        int robDP(vector<int>& nums) {
            if(nums.size()==1)return nums[0];
            vector<int>dp(nums.size());
            dp[0]=nums[0];
            dp[1]=max(nums[0],nums[1]);
            for(int i=2;i<nums.size();i++){
                dp[i]=max(dp[i-1],dp[i-2]+nums[i]);
            }
            return dp[nums.size()-1];
        }

        int robDPOptimized(vector<int>& nums) {
            int n = nums.size();
            if(n == 1) return nums[0];
            
            int prev_ans2=nums[0], prev_ans=max(nums[0],nums[1]),curr_ans=prev_ans;
            
            for(int i = 2; i < n; i++){
                curr_ans = max(prev_ans, prev_ans2 + nums[i]);
                prev_ans2 = prev_ans;
                prev_ans = curr_ans;
            }
            return curr_ans;
        }
};


int main() {

    vector<int> nums = {1,2,3,1};

    Solution solution;
    cout <<  solution.robRecursion(nums) << endl;
    cout <<  solution.robMemo(nums) << endl;

    return 0;
}