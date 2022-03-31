class Solution {

    public static TreeNode searchBST(TreeNode root, int val) {
        if (root == null || val == root.val) return root;

        return val < root.val ? searchBST(root.left, val) : searchBST(root.right, val);
    }

    public static TreeNode searchBSTIterative(TreeNode root, int val) {
        while (root != null && val != root.val)
            root = val < root.val ? root.left : root.right;
        return root;
    }

    private static void inOrder(TreeNode node) {
        if (node == null) {
            return;
        }
        inOrder(node.left);
        System.out.printf("%s ", node.val);
        inOrder(node.right);
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

        int val = 2;
        inOrder(searchBSTIterative(node1, val));

    }
}