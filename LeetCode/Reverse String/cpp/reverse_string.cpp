#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        void reverseStringRecursionHelper(vector<char>& s, int left, int right) {
            if(left < right) {
                swap(s[left], s[right]);
                reverseStringRecursionHelper(s, left+1, right-1);
            }
        }

        void reverseStringRecursion(vector<char>& s) {
            reverseStringRecursionHelper(s, 0, s.size()-1);
        }
};

void print_chr_vec(vector<char>& s)
{
    for (auto s_ptr = s.begin(); s_ptr < s.end(); s_ptr++) {
        cout << *s_ptr;
    }

    cout << endl;
}

int main() {

    vector<char> s{'h','e','l','l','o'};

    Solution solution;
    print_chr_vec(s);
    solution.reverseStringRecursion(s);
    print_chr_vec(s);

    return 0;
}