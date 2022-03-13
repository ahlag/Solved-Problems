public class PalindromePermutation {

    public static boolean checkMaxOneOdd(int[] table) {
        boolean foundOdd = false;
        for (int count : table) {
            if (count % 2 == 1) {
                if (foundOdd) {
                    return false;
                }
                foundOdd = true;
            }
        }
        return true;
    }

    public static boolean isPermutationOfPalindromeCount(String phrase) {
        int[] table = Common.buildCharFrequencyTable(phrase);
        return checkMaxOneOdd(table);
    }

    public static boolean isPermutationOfPalindromeHashTable(String phrase) {
        int countOdd = 0;
        int[] table = new int[Character.getNumericValue('z') - Character.getNumericValue('a') + 1];
        for (char c : phrase.toCharArray()) {
            int x = Common.getCharNumber(c);
            if (x != -1) {
                table[x]++;

                if (table[x] % 2 == 1) {
                    countOdd++;
                } else {
                    countOdd--;
                }
            }
        }
        return countOdd <= 1;
    }

    /* Toggle the ith bit in the integer. */
    public static int toggle(int bitVector, int index) {
        if (index < 0) return bitVector;

        int mask = 1 << index;
        if ((bitVector & mask) == 0) {
            bitVector |= mask;
        } else {
            bitVector &= ~mask;
        }
        return bitVector;
    }

    /* Create bit vector for string. For each letter with value i,
     * toggle the ith bit. */
    public static int createBitVector(String phrase) {
        int bitVector = 0;
        for (char c : phrase.toCharArray()) {
            int x = Common.getCharNumber(c);
            bitVector = toggle(bitVector, x);
        }
        return bitVector;
    }

    /* Check that at most one bit is set by subtracting one from the
     * integer and ANDing it with the original integer. */
    public static boolean checkAtMostOneBitSet(int bitVector) {
        return (bitVector & (bitVector - 1)) == 0;
    }

    public static boolean isPermutationOfPalindromeBit(String phrase) {
        int bitVector = createBitVector(phrase);
        return checkAtMostOneBitSet(bitVector);
    }

    public static void main(String[] args) {
        String palindrome = "Rats live on no evil star";
        System.out.println(isPermutationOfPalindromeHashTable(palindrome));
        System.out.println(isPermutationOfPalindromeCount(palindrome));
        System.out.println(isPermutationOfPalindromeBit(palindrome));
    }
}
