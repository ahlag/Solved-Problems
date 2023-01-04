#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if(s.length() != t.length()) return false;
        unordered_map<char, int> seen;
        for(auto alphabet: s) {
            seen[alphabet]++;
        }

        // for (auto it=seen.begin(); it!=seen.end(); it++) {
        //     cout << it->first << it->second << endl;
        // }
        for(auto alphabet: t) {
            if(seen.find(alphabet) == seen.end()) return false;
            seen[alphabet]--;

            // for (auto it=seen.begin(); it!=seen.end(); it++) {
            //     cout << it->first << it->second << endl;
            // }

            if(seen.find(alphabet)->second < 0) return false;
        }
        return true;
    }
};


int main() {

    string s = "rat";
    string t = "cat";

    Solution solution;
    cout <<  solution.isAnagram(s,t) << endl;

    return 0;
}