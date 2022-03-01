#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        string addStrings(string s1, string s2) {
                int i = s1.size() - 1, j = s2.size() - 1, carry = 0;
                string result;
                // Start from last index
                while (i >= 0 || j >= 0) {
                    int sum = carry;
                    // If i greater than or equal to 0 add integer value of string 1 at that i to sum
                    if (i >= 0) {
                        sum += (s1[i] - '0');
                        i--;
                    }
                    // If j greater than or equal to 0 add integer value of string 2 at that j to sum
                    if (j >= 0) {
                        sum += (s2[j] - '0');
                        j--;
                    }
                    // Add the unit index of sum to result
                    result += to_string(sum % 10);
                    // Carry is equal to sum/10
                    carry = sum / 10;
                }
                
                // If carry is not zero add it to ans as the first char
                if (carry != 0) {
                    result += to_string(carry);
                }
                // reverse string to get the ans
                reverse(result.begin(), result.end());
                return result;
            }
};


int main() {

    string s1 = "101", s2 = "1";

    Solution solution;
    cout <<  solution.addStrings(s1, s2) << endl;

    return 0;
}