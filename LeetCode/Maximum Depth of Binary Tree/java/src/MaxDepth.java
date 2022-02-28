import java.util.LinkedList;

public class MaxDepth {

    public static int maxDepthRecursion(TreeNode root) {

        if (root == null) {
            return 0;
        } else {
            int left_height = maxDepthRecursion(root.left);
            int right_height = maxDepthRecursion(root.right);
            return java.lang.Math.max(left_height, right_height) + 1;
        }
    }

    public static int maxDepthIterative(TreeNode root) {

        LinkedList<TreeNode> stack = new LinkedList<>();
        LinkedList<Integer> depths = new LinkedList<>();
        if (root == null) return 0;

        stack.add(root);
        depths.add(1);

        int depth = 0, current_depth = 0;
        while(!stack.isEmpty()) {
            root = stack.pollLast();
            current_depth = depths.pollLast();
            if (root != null) {
                depth = Math.max(depth, current_depth);
                stack.add(root.left);
                stack.add(root.right);
                depths.add(current_depth + 1);
                depths.add(current_depth + 1);
            }
        }
        return depth;
    }

    public static void main(String[] args) {

        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(9);
        TreeNode node3 = new TreeNode(20);
        TreeNode node4 = new TreeNode(15);
        TreeNode node5 = new TreeNode(7);

        node1.left = node2;
        node1.right = node3;
        node3.left = node4;
        node3.right = node5;

        System.out.println(maxDepthRecursion(node1));
        System.out.println(maxDepthIterative(node1));
    }

}
