import java.util.HashSet;
import java.util.Set;

public class FirstDuplicateValue {

    public static int firstDuplicateValueHashSet(int[] array) {
        Set<Integer> found = new HashSet<>();
        for(int i = 0; i < array.length - 1; i++) {
            if (found.contains(array[i])) return array[i];
            found.add(array[i]);
        }
        return -1;
    }

    public static int firstDuplicateValueOptimized(int[] array) {
        for (int value : array) {
            int absValue = Math.abs(value);
            if( array[absValue-1] < 0) {
                return absValue;
            }
            array[absValue-1] *= -1;
        }
        return -1;
    }

    public static void main(String[] args) {

        int[] array = {2, 1, 5, 2, 3, 3, 4};

        System.out.println(firstDuplicateValueHashSet(array));
        System.out.println(firstDuplicateValueOptimized(array));
    }

}
