package reverseBits;

class ReverseBits {
    public int reverseBits(int input) {

    int output = 0;

    while (input != 0) {
        output = output << 1;

        if ((input & 1) == 1) {
            output |= 1;
        }

        input = input >> 1;
    }

        return output;
    }
}