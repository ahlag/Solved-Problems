#include <bits/stdc++.h>
#include <assert.h>

using namespace std;

class Solution {
    public:
        vector<int> searchInSortedMatrix(vector<vector<int>> matrix, int target) {
            int row = 0;
            int col = matrix[0].size() - 1;
            while(row < matrix.size() && col >= 0) {
                if(matrix[row][col] > target) {
                    col--;
                } else if (matrix[row][col] < target) {
                    row++;
                } else {
                    return {row, col};
                }
            }
            return {-1,-1};
        }
};

int main() {

    vector<vector<int>> matrix{
                                {1, 4, 7, 12, 15, 1000},        
                                {2, 5, 19, 31, 32, 1001},
                                {3, 8, 24, 33, 35, 1002},
                                {40, 41, 42, 44, 45, 1003},
                                {99, 100, 103, 106, 128, 1004},
    };
    vector<int> expected{3, 3};
    

    Solution solution;
    vector<int> res = solution.searchInSortedMatrix(matrix, 44);
    assert(res == expected);

    for(auto ele: res)
        cout << ele << " ";

    return 0;
}