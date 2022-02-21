import java.util.Arrays;

public class SquaresOfASortedArray {

    public static int[] squaresOfASortedArray(int[] nums) {

        int N = nums.length;
        int[] res = new int[N];

        for(int i = 0; i < N; i++) {
            res[i] = nums[i] * nums[i];
        }

        Arrays.sort(res);

        return res;
    }

    public static int[] squaresOfASortedTwoPointers(int[] nums) {

        int N = nums.length;
        int i = 0, j = N - 1;
        int k = N - 1;

        int first_square, second_square;

        int[] res = new int[N];

        while (i <= j) {

            first_square = nums[i] * nums[i];
            second_square = nums[j] * nums[j];

            if(first_square <= second_square) {
                res[k] = second_square;
                j--;
            } else {
                res[k] = first_square;
                i++;
            }
            k--;
        }

        return res;
    }

    public static void main(String[] args) {

        int[] nums = {-7, -3, 2, 3, 11};

        System.out.println(Arrays.toString(squaresOfASortedTwoPointers(nums)));
        System.out.println(Arrays.toString(squaresOfASortedArray(nums)));
    }

}
