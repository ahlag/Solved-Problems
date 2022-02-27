public class IsUnique {

    public static boolean isUniqueChars(String str) {
        if (str.length() > 128) {
            return false;
        }
        boolean[] char_set = new boolean[128];
        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i) - 'a';
            if (char_set[val]) return false;
            char_set[val] = true;
        }
        return true;
    }

    /* Assumes only letters a through z. */
    public static boolean isUniqueCharsBitVector(String str) {
        if (str.length() > 128) {
            return false;
        }
        int checker = 0;
        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i) - 'a';
            if ((checker & (1 << val)) > 0) return false;
            checker |= (1 << val);
        }
        return true;
    }

}
