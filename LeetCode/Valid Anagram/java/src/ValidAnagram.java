import java.util.HashMap;
import java.util.Map;

public class ValidAnagram {

    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] table = new int[26];
        for (int i = 0; i < s.length(); i++) {
            table[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            table[t.charAt(i) - 'a']--;
            if (table[t.charAt(i) - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }

    public boolean isAnagramShorter(String s, String t) {

        if(s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> seen = new HashMap<>();
        for(char alphabet: s.toCharArray()) {
            seen.merge(alphabet, 1, (a, b) -> a + b);
        }

        for(char alphabet: t.toCharArray()) {
            if (seen.containsKey(alphabet) == false) return false;
            seen.put(alphabet, seen.get(alphabet) - 1);
            if (seen.get(alphabet) < 0) return false;
        }

        return true;
    }

    public static void main(String[] args) {
        String s = "abcd";
        String t = "ggge";

        System.out.println(isAnagram(s,t));

    }
}
