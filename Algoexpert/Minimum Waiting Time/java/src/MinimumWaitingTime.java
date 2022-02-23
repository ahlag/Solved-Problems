import java.util.Arrays;

public class MinimumWaitingTime {

    public static int minimumWaitingTime(int[] queries) {

        Arrays.sort(queries);

        int totalWaitingTime = 0;
        for(int i = 0; i < queries.length; i++) {
            int queriesLeft = queries.length - (i+1);
            totalWaitingTime += queriesLeft * queries[i];
        }

        return totalWaitingTime;
    }


    public static void main(String[] args) {

        int[] queries = {3,2,1,2,6};

        System.out.println(minimumWaitingTime(queries));
    }
}
