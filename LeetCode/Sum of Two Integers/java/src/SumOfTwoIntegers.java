public class SumOfTwoIntegers {

    public static int getSumBit(int x, int y) {

        while (y != 0) {

            int carry = x & y;

            x = x ^ y;

            y = carry << 1;
        }

        return x;
    }

    public static int getSumLanguageIndependent(int a, int b) {
        int x = Math.abs(a), y = Math.abs(b);
        // ensure that abs(a) >= abs(b)
        if (x < y) return getSumLanguageIndependent(b, a);

        // abs(a) >= abs(b) -->
        // a determines the sign
        int sign = a > 0 ? 1 : -1;

        if (a * b >= 0) {
            // sum of two positive integers x + y
            // where x > y
            while (y != 0) {
                int answer = x ^ y;
                int carry = (x & y) << 1;
                x = answer;
                y = carry;
            }
        } else {
            // difference of two positive integers x - y
            // where x > y
            while (y != 0) {
                int answer = x ^ y;
                int borrow = ((~x) & y) << 1;
                x = answer;
                y = borrow;
            }
        }
        return x * sign;
    }

    public static void main(String[] args) {

        int x = 2, y = 3;

        int nx = 2, ny = -3;

        System.out.println(getSumBit(x, y));
        System.out.println(getSumBit(nx, ny));
        System.out.println(getSumLanguageIndependent(x,y));
        System.out.println(getSumLanguageIndependent(nx,ny));
    }

}
