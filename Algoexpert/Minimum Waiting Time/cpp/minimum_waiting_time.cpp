#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
    int minimumWaitingTime(vector<int>& queries) {
        
        sort(queries.begin(), queries.end());
        int totalWaitingTime = 0;

        for(size_t i = 0; i < queries.size(); i++) {
            int queriesLeft = queries.size() - (i+1);
            totalWaitingTime += queriesLeft * queries[i];
        }

        return totalWaitingTime;
    }
    
};

int main() {

    vector<int> queries = {3, 2, 1, 2, 6};

    Solution solution;

    cout << solution.minimumWaitingTime(queries) << endl;

    return 0;
}