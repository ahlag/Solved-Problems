#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        int mySqrtBinarySearch(int x) {

            if (x < 2)
                return 2;

            int left = 2, right = x / 2;
            
            while (left <= right) {

                int pivot = left + (right - left)/2;
                int num = pivot * pivot;

                if(num > x) {
                    right = pivot - 1;
                } else if (num < x) {
                    left = pivot + 1;
                } else{
                    return pivot;
                }

            }
            
            return right;
        }
};


int main() {

    int num = 8;

    Solution solution;
    cout <<  solution.mySqrtBinarySearch(num) << endl;

    return 0;
}