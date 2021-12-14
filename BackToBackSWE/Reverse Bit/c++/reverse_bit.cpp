#include <iostream>

using namespace std;

int reverseBits(int input) {

    int output = 0;

    while (input != 0) {
        output = output << 1;

        if ((input & 1) == 1) {
            output |= 1;
        }

        input = input >> 1;
    }

    return output;
};

int main() {

    int inputs[] = { 1, 10, 9090 };

    for(auto & input: inputs) {
        cout << reverseBits(input) << endl;
    }

    return 0;
}