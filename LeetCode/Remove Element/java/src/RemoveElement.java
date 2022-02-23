public class RemoveElement {

    public static int removeElement(int[] nums, int val) {
        int i = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }

    public static int removeElementOptimize(int[] nums, int val) {
        int i = 0;
        int n = nums.length;
        while (i < n) {
            if (nums[i] == val) {
                nums[i] = nums[n - 1];
                // reduce array size by one
                n--;
            } else {
                i++;
            }
        }
        return n;
    }

    public static void main(String[] args) {

        int[] nums1 = {3,2,2,3};
        int val = 3;

        System.out.println(removeElement(nums1, val));

        int[] nums2 = {3,2,2,3};
        System.out.println(removeElementOptimize(nums2, val));
    }
}
