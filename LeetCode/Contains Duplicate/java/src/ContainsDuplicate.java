import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;

public class ContainsDuplicate {

    public static boolean containsDuplicateArray(int[] nums) {
        Arrays.sort(nums);
        for(int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i+1]) return true;
        }

        return false;
    }

    public static boolean containsDuplicateHashSet(int[] nums) {

        Set<Integer> set = new HashSet<>(nums.length);

        for (int num : nums) {
            if (set.contains(num)) return true;
            set.add(num);
        }

        return false;
    }

    public static void main(String[] args) {

        int[] nums = {1,2,3,1};

        System.out.println(containsDuplicateArray(nums));
        System.out.println(containsDuplicateHashSet(nums));
    }

}
