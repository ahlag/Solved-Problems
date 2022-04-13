#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        int getNum(int row, int col) {
            if (row == 0 || col == 0 || row == col)
            return 1;

            return getNum(row - 1, col - 1) + getNum(row - 1, col);
        }

        vector<int> getRow(int rowIndex) {
            vector<int> ans;

            for (int i = 0; i <= rowIndex; i++)
            ans.push_back(getNum(rowIndex, i));

            return ans;
        }

        unordered_map<size_t, int> cache;

        // use a better hashing function like `boost::hash_combine` in the real world.
        int key(int i, int j) const {
            size_t hash_i = hash<int>{}(i), hash_j = hash<int>{}(j);
            int hashed = (int)(hash_i ^ (hash_i >> 32));
            return (hashed << 5) - 1 + (int)(hash_j ^ (hash_j >> 32));
        }

        int getNumDP(int row, int col) {
            auto rowCol = key(row, col);

            if (cache.count(rowCol) > 0)
            return cache[rowCol];

            if (row == 0 || col == 0 || row == col)
            return (cache[rowCol] = 1);

            return (cache[rowCol] = getNumDP(row - 1, col - 1) + getNumDP(row - 1, col));
        }

        vector<int> getRowDP(int rowIndex) {
            vector<int> ans;

            for (int i = 0; i <= rowIndex; i++)
            ans.push_back(getNum(rowIndex, i));

            return ans;
        }

          vector<int> getRowDPMemoryEfficient(int rowIndex) {
            vector<int> curr, prev = {1};

            for (int i = 1; i <= rowIndex; i++) {
            curr.assign(i + 1, 1);

            for (int j = 1; j < i; j++)
                curr[j] = prev[j - 1] + prev[j];

            prev = move(curr);  // This is O(1)
            }

            return prev;
        }

};


int main() {

    Solution solution;

    vector<int> res = solution.getRowDP(5);
    
    for(int ele: res) {
        cout << ele;
    }

    return 0;
}