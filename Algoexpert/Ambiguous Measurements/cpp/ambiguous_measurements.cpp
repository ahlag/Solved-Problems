#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:

        bool ambiguousMeasurements(vector<vector<int>> measuringCups, int low, int high) {
            unordered_map<string, bool> memoization;
            return canMeasureInRange(measuringCups, low, high, memoization);
        }

        bool canMeasureInRange(vector<vector<int>> &measuringCups, 
                                int low, 
                                int high, 
                                unordered_map<string, bool> &memoization) {
            string memoizeKey = createHashableKey(low, high);
            if(memoization.find(memoizeKey) != memoization.end()) {
                return memoization[memoizeKey];
            }

            if(low <= 0 && high <= 0) {
                return false;
            }

            bool canMeasure = false;

            for(auto cup: measuringCups) {
                int cupLow = cup[0];
                int cupHigh = cup[1];
                if (low <= cupLow && cupHigh <= high) {
                    canMeasure = true;
                    break;
                }

                int newLow = max(0, low - cupLow);
                int newHigh = max(0, high - cupHigh);
                canMeasure = canMeasureInRange(measuringCups, newLow, newHigh, memoization);

                if(canMeasure) break;
            }

            memoization[memoizeKey] = canMeasure;
            return canMeasure;
        }

        string createHashableKey(int low, int high) {
            return to_string(low) + ":" + to_string(high);
        }

};


int main() {

    vector<vector<int>> cups = {{200, 210}, {450, 465}, {800, 850}};
    int low = 2100;
    int high = 2300;

    Solution solution;
    cout <<  solution.ambiguousMeasurements(cups, low, high) << endl;

    return 0;
}