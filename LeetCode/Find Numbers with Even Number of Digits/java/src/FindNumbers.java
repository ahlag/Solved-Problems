public class FindNumbers {

    public static int findNumbers(int[] nums) {

        int cnt = 0;

        for (int num : nums) {

            int subcnt = 0;
            while(num != 0) {
                num /= 10;
                subcnt++;
            }
            if(subcnt%2==0) cnt++;
        }

        return cnt;
    }

    public static int findNumbersMath(int[] nums) {

        int result = 0;

        for(int i = 0 ; i < nums.length ; i++){

            int count = (int)Math.log10(nums[i]) + 1; //example (234 log 10 + 1) = ( 2 + 1 ) = 3 - number of digit
            if(count % 2 == 0) result++;
        }

        return result;
    }

    public static void main(String[] args) {

        int[] nums = {12,345,2,6,7896};

        System.out.println(findNumbers(nums));
        System.out.println(findNumbersMath(nums));
    }
}
