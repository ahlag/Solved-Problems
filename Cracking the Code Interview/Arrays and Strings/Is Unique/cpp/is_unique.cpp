#include <bits/stdc++.h>

using namespace std;

bool isUniqueChars(const string &str){
		if (str.length() > 128){
			return false;
		}
		vector<bool> char_set(128);
		for (size_t i = 0; i < str.length(); i++){
			int val = str[i];
			if (char_set[val]){
				return false;
			}
			char_set[val] = true;
		}
		return true;
}

bool isUniqueCharsBitvector(const string &str) {
    //Reduce space usage by a factor of 8 using bitvector. 
	//Each boolean otherwise occupies a size of 8 bits.

    bitset<256> bits(0);
    for(size_t i = 0; i < str.length(); i++) {
        int val = str[i];
        if (bits.test(val) > 0) {
            return false;
        }
        bits.set(val);
    }

    return true;
}

int main(){
	
    vector<string> words = {"abcde", "hello", "apple", "kite", "padle"};

    for (auto word : words) {
		cout << word << string(": ") << boolalpha << isUniqueChars(word) <<endl;
	}

	cout <<endl << "Using bit vector" <<endl;
	
    for (auto word : words) {
		cout << word << string(": ") << boolalpha << isUniqueCharsBitvector(word) <<endl;
	}

    return 0;
}