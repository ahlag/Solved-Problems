import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class NumberOfBinaryTreeTopologies {

    public static int numberOfBinaryTreeTopologiesRecursion(int n) {

        if (n == 0)	return 1;

        int numberOfTrees = 0;
        for (int leftTreeSize = 0; leftTreeSize < n; leftTreeSize++) {
            int rightTreeSize = n - 1 - leftTreeSize;
            int numberOfLeftTrees = numberOfBinaryTreeTopologiesRecursion(leftTreeSize);
            int numberOfRightTrees = numberOfBinaryTreeTopologiesRecursion(rightTreeSize);
            numberOfTrees += numberOfLeftTrees * numberOfRightTrees;
        }

        return numberOfTrees;
    }

    public static int numberOfBinaryTreeTopologiesMemo(int n) {
        Map<Integer, Integer> cache = new HashMap<Integer, Integer>();
        cache.put(0, 1);
        return helper(n, cache);
    }

    public static int helper(int n, Map<Integer,Integer> cache) {
        if (cache.containsKey(n))   return cache.get(n);

        int numberOfTrees = 0;
        for (int leftTreeSize = 0; leftTreeSize < n; leftTreeSize++) {
            int rightTreeSize = n - 1 - leftTreeSize;
            int numberOfLeftTrees = helper(leftTreeSize, cache);
            int numberOfRightTrees = helper(rightTreeSize, cache);
            numberOfTrees += numberOfLeftTrees * numberOfRightTrees;
        }
        cache.put(n, numberOfTrees);
        return cache.get(n);
    }

    public static int numberOfBinaryTreeTopologiesOptimized(int n) {

        List<Integer> cache = new ArrayList<Integer>();
        cache.add(1);
        for(int m = 1; m <= n; m++) {
            int numberOfTrees = 0;
            for (int leftTreeSize = 0; leftTreeSize < m; leftTreeSize++) {
                int rightTreeSize = m - 1 - leftTreeSize;
                int numberOfLeftTrees = cache.get(leftTreeSize);
                int numberOfRightTrees = cache.get(rightTreeSize);
                numberOfTrees += numberOfLeftTrees * numberOfRightTrees;
            }
            cache.add(numberOfTrees);
        }

        return cache.get(n);
    }

    public static void main(String[] args) {
        int n = 3;

        System.out.println(numberOfBinaryTreeTopologiesRecursion(n));
        System.out.println(numberOfBinaryTreeTopologiesMemo(n));
        System.out.println(numberOfBinaryTreeTopologiesOptimized(n));
    }


}
