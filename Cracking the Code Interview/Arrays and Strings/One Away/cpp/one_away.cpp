#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        bool oneEditAway( const string & str1, const string & str2 ) {
            if ( abs( int(str1.length()) - int(str2.length()))  > 1 ) {
                return false;
            }

            int len1 = str1.length();
            int len2 = str2.length();
            string smaller = len1 < len2 ? str1 : str2;
            string bigger =  len1 < len2 ? str2 : str1;
            
            unsigned int i = 0, j = 0; 
            bool mismatchDone = false;
            while ( i < smaller.length() && j < bigger.length() )
            {
                if ( smaller[i] != bigger[j] ) {
                    if (mismatchDone) {
                        return false;
                    }
                    mismatchDone = true;
                    if ( len1 == len2 ) {
                        ++i;   //case of replace
                    }
                } else {
                        ++i;   //move short pointer if its a match, dont move it in case of first mismatch
                }
                ++j;           //always move long string pointer.
            }
            return true;
        }

        void translate( bool result, const string str1, const string str2 ) {
            if (result == true ) {
                cout << str1 << " and " << str2 << " are one edit away\n";
            } else {
                cout << str1 << " and " << str2 << " are not one edit away\n";
            }
        }

};


int main() {

    Solution solution;
    vector<int> num = {-1,0,1,2,-1,-4};    
    solution.translate ( solution.oneEditAway("pale", "ple"), "pale", "ple" );
    solution.translate ( solution.oneEditAway("pales", "pale"), "pales", "pale" );
    solution.translate ( solution.oneEditAway("pale", "pales"), "pale", "pales" );
    solution.translate ( solution.oneEditAway("pale", "bale"), "pale", "bale" );
    solution.translate ( solution.oneEditAway("pale", "bake"), "pale", "bake" );
    return 0;
}