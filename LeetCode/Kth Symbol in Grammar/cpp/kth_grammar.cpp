#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        int kthGrammar(int N, int K) {
            if (N == 1) return 0;
            if (K % 2 == 0) return (kthGrammar(N - 1, K / 2) == 0) ? 1 : 0;
            else return (kthGrammar(N - 1, (K + 1) / 2) == 0) ? 0 : 1;
    }
}


int main() {

    Solution solution;

    int n = 3, k = 2;

    cout << solution.kthGrammar(n, k) << endl;

    return 0;
}