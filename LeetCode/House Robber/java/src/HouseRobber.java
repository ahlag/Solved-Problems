public class HouseRobber {

    public static void main(String[] args) {

        int[] nums = {1,2,3,1};

        HouseRobberDynamicProgramming sol1 = new HouseRobberDynamicProgramming();
        HouseRobberMemoization sol2 = new HouseRobberMemoization();
        HouseRobberOptimizedDynamicProgramming sol3 = new HouseRobberOptimizedDynamicProgramming();

        System.out.println(sol1.rob(nums));
        System.out.println(sol2.rob(nums));
        System.out.println(sol3.rob(nums));
    }

}
