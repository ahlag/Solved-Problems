public class Tester {

    public static void main(String[] args) {
        String[] words = {"abcde", "hello", "apple", "kite", "padle"};
        for (String word : words) {
            boolean wordA =  IsUnique.isUniqueChars(word);
            boolean wordB =  IsUnique.isUniqueCharsBitVector(word);

            if (wordA == wordB) {
                System.out.println(word + ": " + wordA);
            } else {
                System.out.println(word + ": " + wordA + " vs " + wordB);
            }
        }
    }

}
