#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
    int removeElement(vector<int>& arr, int val) {
        
        int i = 0;
        for(size_t j = 0; j < arr.size(); j++) {
            if (arr[j] != val) {
                arr[i] = arr[j];
                i++;
            }
        }

        return i;
    }

    int removeElementOptimize(vector<int>& arr, int val) {
        
        int i = 0;
        int n = arr.size();

        while (i < n) {
            if(arr[i] == val) {
                arr[i] = arr[n-1];
                n--;
            } else {
                i++;
            }

        }

        return n;
    }
    
};

int main() {

    vector<int> nums = {3,2,2,3};
    int val = 3;

    Solution solution;

    cout << solution.removeElement(nums, val) << endl;
    
    nums = {3,2,2,3};
    cout << solution.removeElementOptimize(nums, val) << endl;

    return 0;
}