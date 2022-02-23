public class ReverseString {

    public static void helper(char[] s, int left, int right) {
        if (left >= right) return;
        char tmp = s[left];
        s[left++] = s[right];
        s[right--] = tmp;
        helper(s, left, right);
    }

    public static void reverseString(char[] s) {
        helper(s, 0, s.length - 1);
    }

    public static void reverseStringIterative(char[] s) {
        int left = 0, right = s.length - 1;
        while (left < right) {
            char tmp = s[left];
            s[left++] = s[right];
            s[right--] = tmp;
        }
    }

    public static void main(String[] args) {

        char[] string = {'h','e','l','l','o'};

        reverseString(string);
        System.out.println(string);
    }

}
