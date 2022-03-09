#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        int firstDuplicateValueHashSet(vector<int> array) {
            unordered_map<int, bool> seen;
            for(int value : array) {
                if (seen.find(value) != seen.end()) {
                    return value;
                }
                seen[value] = true;
            }
            return -1;
        }

        int firstDuplicateValueOptimized(vector<int> array) {
            for (int value : array) {
                int absValue = abs(value);
                if( array[absValue-1] < 0) {
                    return absValue;
                }
                array[absValue-1] *= -1;
            }
            return -1;
        }
};


int main() {

    vector<int> array = {2, 1, 5, 2, 3, 3, 4};

    Solution solution;
    cout <<  solution.firstDuplicateValueHashSet(array) << endl;
    cout <<  solution.firstDuplicateOptimized(array) << endl;

    return 0;
}