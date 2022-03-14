#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        int longestPeak(vector<int> &array) {

        int i = 1;
        int n = array.size();
        int longestPeakLength = 0;

        while (i < n - 1) {
            bool isPeak = array[i-1] < array[i] && array[i] > array[i+1];
            if (!isPeak) {
                i++;
                continue;
            }

            int leftIdx = i - 2;
            while(leftIdx >= 0 && array[leftIdx] < array[leftIdx+1]) {
                leftIdx -= 1;
            }

            int rightIdx = i + 2;
            while (rightIdx < n && array[rightIdx] < array[rightIdx-1]) {
                rightIdx += 1;
            }
            int currentPeakLength = rightIdx - leftIdx - 1;
            longestPeakLength = max(currentPeakLength, longestPeakLength);
            i = rightIdx;
        }

        return longestPeakLength;
    }

};


int main() {

    vector<int> input = {1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3};

    Solution solution;
    cout <<  solution.longestPeak(input) << endl;

    return 0;
}