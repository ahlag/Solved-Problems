import java.util.Arrays;

public class MoveZeroes {

//    public static boolean containsDuplicateArray(int[] nums) {
//        Arrays.sort(nums);
//        for(int i = 0; i < nums.length - 1; i++) {
//            if (nums[i] == nums[i+1]) return true;
//        }
//
//        return false;
//    }

    public static void moveZeroesSuboptimal(int[] nums) {

        int count = 0, size = nums.length;

        for (int i = 0; i< size; i++) {
            if ( nums[i] == 0) { count ++;}
            if ( nums[i] != 0) { nums[i - count] = nums[i];}
        }

        for (int i = 0; i < count; i++ ) {
            nums[size - count  + i] = 0;
        }
    }

    public static void moveZeroesOptimal(int[] nums) {

        int count=0;
        for(int i=0;i<nums.length;i++){

            if(nums[i]!=0){
                int temp=nums[i];
                nums[i]=nums[count];
                nums[count]=temp;
                count++;
            }
        }
    }

    public static void main(String[] args) {

        int[] nums = {0,1,0,3,12};

        moveZeroesOptimal(nums);

        System.out.println(Arrays.toString(nums));
    }

}
