import java.util.*;

public class PascalTriangle {

    public static int calculate(int row, int col) {

        if(row == 0 || col == 0 || row == col) {
            return 1;
        }

        return calculate(row-1, col) + calculate(row-1, col-1);
    }

    public static List<Integer> getRow(int rowIndex) {
        ArrayList<Integer> res = new ArrayList<>();
        for(int i = 0; i < rowIndex+1; i++) {
            res.add(calculate(rowIndex, i));
        }
        return res;
    }

    // Dynamic Programming
    private static class RowCol {
        private int row, col;

        public RowCol(int row, int col) {
            this.row = row;
            this.col = col;
        }

        @Override
        public int hashCode() {
            int result = (int) (row ^ (row >>> 32));
            return (result << 5) - 1 + (int) (col ^ (col >>> 32)); // 31 * result == (result << 5) - 1
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null) return false;
            if (this.getClass() != o.getClass()) return false;

            RowCol rowCol = (RowCol) o;
            return row == rowCol.row && col == rowCol.col;
        }
    }

    private static Map<RowCol, Integer> cache = new HashMap<>();

    private static int getNum(int row, int col) {
        RowCol rowCol = new RowCol(row, col);

        if (cache.containsKey(rowCol)) {
            return cache.get(rowCol);
        }

        int computedVal =
                (row == 0 || col == 0 || row == col) ? 1 : getNum(row - 1, col - 1) + getNum(row - 1, col);

        cache.put(rowCol, computedVal);

        return computedVal;
    }

    public static List<Integer> getRowDP(int rowIndex) {
        List<Integer> ans = new ArrayList<>();

        for (int i = 0; i <= rowIndex; i++) {
            ans.add(getNum(rowIndex, i));
        }

        return ans;
    }

    public List<Integer> getRowDPMemoryEfficient(int rowIndex) {
        List<Integer> row =
                new ArrayList<>(rowIndex + 1) {
                    {
                        add(1);
                    }
                };

        for (int i = 0; i < rowIndex; i++) {
            for (int j = i; j > 0; j--) {
                row.set(j, row.get(j) + row.get(j - 1));
            }
            row.add(1);
        }

        return row;
    }

    public List<Integer> getRowMath(int rowIndex) {
        List<Integer> row =
                new ArrayList<>(rowIndex + 1) {
                    {
                        add(1);
                    }
                };

        for (int i = 0; i < rowIndex; i++) {
            for (int j = i; j > 0; j--) {
                row.set(j, row.get(j) + row.get(j - 1));
            }
            row.add(1);
        }

        return row;
    }

    public static void main(String[] args) {
        int val = 5;
        System.out.println(Arrays.toString(getRow(5).toArray()));
        System.out.println(Arrays.toString(getRowDP(5).toArray()));
    }
}
