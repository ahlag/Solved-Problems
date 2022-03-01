public class AddStrings {

    public static String addStrings(String s1, String s2) {
        int i = s1.length() - 1, j = s2.length() - 1, carry = 0;

        /* Strings are immutable in Java, so use StringBuilder for efficiency. */
        StringBuffer result = new StringBuffer("");

        while (i >= 0 || j >= 0) {
            int sum = carry;
            // If i greater than or equal to 0 add integer value of string 1 at that i to sum
            if (i >= 0) {
                sum += (s1.charAt(i) - '0');
                i--;
            }
            // If j greater than or equal to 0 add integer value of string 2 at that j to sum
            if (j >= 0) {
                sum += (s2.charAt(j) - '0');
                j--;
            }
            // add result to sum
            result.append(sum % 10);
            // carry is sum/10
            carry = sum / 10;
        }
        // if carry is not zero add it as the last char
        if (carry != 0) {
            result.append(carry);
        }
        return result.reverse().toString();
    }

    public static void main(String[] args) {

        String s1 = "101", s2 = "9";

        System.out.println(addStrings(s1, s2));
    }


}
