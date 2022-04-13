import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;

public class isValidBST {

    public boolean validateValidRangeRecursive(TreeNode root, Integer low, Integer high) {
        // Empty trees are valid BSTs.
        if (root == null) {
            return true;
        }
        // The current node's value must be between low and high.
        if ((low != null && root.val <= low) || (high != null && root.val >= high)) {
            return false;
        }
        // The left and right subtree must also be valid.
        return validateValidRangeRecursive(root.right, root.val, high) && validateValidRangeRecursive(root.left, low, root.val);
    }

    public boolean isValidBSTValidRangeRecursive(TreeNode root) {
        return validateValidRangeRecursive(root, null, null);
    }

    private Deque<TreeNode> stack = new LinkedList();
    private Deque<Integer> upperLimits = new LinkedList();
    private Deque<Integer> lowerLimits = new LinkedList();

    public void update(TreeNode root, Integer low, Integer high) {
        stack.add(root);
        lowerLimits.add(low);
        upperLimits.add(high);
    }

    public boolean isValidBSTValidRangeIterative(TreeNode root) {
        Integer low = null, high = null, val;
        update(root, low, high);

        while (!stack.isEmpty()) {
            root = stack.poll();
            low = lowerLimits.poll();
            high = upperLimits.poll();

            if (root == null) continue;
            val = root.val;
            if (low != null && val <= low) {
                return false;
            }
            if (high != null && val >= high) {
                return false;
            }
            update(root.right, val, high);
            update(root.left, low, val);
        }
        return true;
    }

    // We use Integer instead of int as it supports a null value.
    private Integer prev;

    public boolean isValidBSTRecursive(TreeNode root) {
        prev = null;
        return inorderRecursive(root);
    }

    private boolean inorderRecursive(TreeNode root) {
        if (root == null) {
            return true;
        }
        if (!inorderRecursive(root.left)) {
            return false;
        }
        if (prev != null && root.val <= prev) {
            return false;
        }
        prev = root.val;
        return inorderRecursive(root.right);
    }

    public static boolean isValidBSTIterative(TreeNode root) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        Integer prev = null;

        while (!stack.isEmpty() || root != null) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            // If next element in inorder traversal
            // is smaller than the previous one
            // that's not BST.
            if (prev != null && root.val <= prev) {
                return false;
            }
            prev = root.val;
            root = root.right;
        }
        return true;
    }

    public static void main(String[] args) {
        TreeNode node1 = new TreeNode(4);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(7);
        TreeNode node4 = new TreeNode(1);
        TreeNode node5 = new TreeNode(3);

        node1.left = node2;
        node1.right = node3;
        node2.left = node4;
        node2.right = node5;

        System.out.println(isValidBSTIterative(node1));
    }

}
