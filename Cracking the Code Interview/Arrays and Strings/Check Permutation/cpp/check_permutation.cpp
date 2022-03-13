#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        bool check_permutation_by_sort(string str1,string str2) {
            // Get lengths of both strings
            int n1 = str1.length();
            int n2 = str2.length();

            // If length of both strings is not same, then they
            // cannot be anagram
            if (n1 != n2)
            return false;

            // Sort both strings
            sort(str1.begin(), str1.end());
            sort(str2.begin(), str2.end());
            // Compare sorted strings
            for (int i = 0; i < n1;  i++)
            if (str1[i] != str2[i])
                return false;

            return true;
        }

        bool check_permutation_by_count(const string &str1, const string &str2) {
            if(str1.length() != str2.length()) 
                return false;
            int count[256]={0};
            for(int i = 0; i < str1.length(); i++) {
                int val = str1[i];
                count[val]++;
            }
            for(int i = 0; i < str2.length(); i++) {
                int val = str2[i];
                count[val]--;
                if(count[val]<0) 
                return false;
            }
            return true;
        }

};


int main() {

    vector<int> num = {-1,0,1,2,-1,-4};

    Solution solution;
    
    cout << "Method 1 - Using sort" << endl;
    string str1 = "testest";
    string str2 = "estxest";
    if(solution.check_permutation_by_sort(str1, str2))
        cout << str1 <<" and " << str2 << " are permutation of each other" << endl;
    else
        cout << str1 <<" and " << str2 << " are not permutation of each other" << endl;
    str1 = "hello";
    str2 = "oellh";
    if(solution.check_permutation_by_sort(str1, str2))
        cout << str1 <<" and " << str2 << " are permutation of each other" << endl;
    else
        cout << str1 <<" and " << str2 << " are not permutation of each other" << endl;

    //Test Method 2 - Using character count
    cout << "Method 2 - Using character count" << endl;
    str1 = "testest";
    str2 = "estxest";
    if(solution.check_permutation_by_count(str1, str2))
        cout << str1 <<" and " << str2 << " are permutation of each other" << endl;
    else
        cout << str1 <<" and " << str2 << " are not permutation of each other" << endl;
    str1 = "hello";
    str2 = "oellh";
    if(solution.check_permutation_by_count(str1, str2))
        cout << str1 <<" and " << str2 << " are permutation of each other" << endl;
    else
        cout << str1 <<" and " << str2 << " are not permutation of each other" << endl;
    
    return 0;
}