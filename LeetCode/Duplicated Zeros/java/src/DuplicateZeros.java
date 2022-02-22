import java.util.Arrays;

public class DuplicateZeros {
    /*
        O(n) runtime
        O(1) space
    */
    public static int[] duplicateZeros(int[] A) {

        int n = A.length, count = 0;

        for (int num : A) if (num == 0) count++;
        int i = n - 1;
        int write = n + count - 1;

        while (i >= 0 && write >= 0)  {

            if (A[i] != 0) { // Non-zero, just write it in
                if (write < n) A[write] = A[i];

            } else { // Zero found, write it in twice if we can
                if (write < n) A[write] = A[i];
                write--;
                if (write < n) A[write] = A[i];
            }

            i--;
            write--;
        }

        return A;
    }

    public static void main(String[] args) {

        int[] nums = {1,0,2,3,0,4,5,0};

        System.out.println(Arrays.toString(duplicateZeros(nums)));
    }

}
