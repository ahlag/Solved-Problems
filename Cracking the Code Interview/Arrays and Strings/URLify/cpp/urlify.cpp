#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        void urlify(char *str, int len) {
            int numOfSpaces = 0;
            int i = 0, j = 0;
            for ( i = 0; i < len; ++i ) {
                if (str[i] == ' ') {
                    ++numOfSpaces;
                }
            }
            
            int extendedLen  = len + 2 * numOfSpaces;
            i = extendedLen - 1;
            for( j = len - 1; j >= 0; --j ) {
                if ( str[j] != ' ' ) {
                str[i--] = str[j];
                } else {
                    str[i--] = '0';
                    str[i--] = '2';
                    str[i--] = '%';
                }
            }
        }

};


int main() {

    Solution solution;
    char str[] = "Mr John Smith    ";                       //String with extended length ( true length + 2* spaces)
    cout << "Actual string   : " << str << std::endl;
    solution.urlify(str, 13);                                        //Length of "Mr John Smith" = 13
    cout << "URLified string : " << str << std::endl;
    return 0;
}