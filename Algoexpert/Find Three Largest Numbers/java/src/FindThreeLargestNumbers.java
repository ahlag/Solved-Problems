import java.util.Arrays;

public class FindThreeLargestNumbers {

    public static int[] findThreeLargestNumbers(int[] array) {
        int[] threeLargest = {Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE};
        for (int num: array) {
            updateLargest(threeLargest, num);
        }
        return threeLargest;
    }

    public static void updateLargest(int[] threeLargest, int num) {
        if (num > threeLargest[2]) {
            shiftAndUpdate(threeLargest, num, 2);
        } else if (num > threeLargest[1]){
            shiftAndUpdate(threeLargest, num, 1);
        } else if (num > threeLargest[0]){
            shiftAndUpdate(threeLargest, num, 0);
        }
    }

    public static void shiftAndUpdate(int[] threeLargest, int num, int idx) {
        for (int i = 0; i <= idx; i++ ) {
            if(i == idx) {
                threeLargest[i] = num;
            } else {
                threeLargest[i] = threeLargest[i+1];
            }
        }
    }

    public static void main(String[] args) {

        int[] x = {141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7};

        System.out.println(Arrays.toString(findThreeLargestNumbers(x)));
    }

}
