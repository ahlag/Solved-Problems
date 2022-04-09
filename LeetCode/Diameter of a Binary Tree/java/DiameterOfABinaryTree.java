public class DiameterOfABinaryTree {

    private static int diameter = 0;
    public static int diameterOfBinaryTree(TreeNode root) {
        diameterOfBinaryTreeHelper(root);
        return diameter;
    }

    public static int diameterOfBinaryTreeHelper(TreeNode root) {

        if(root==null) {
            return 0;
        }

        int leftHeight = diameterOfBinaryTreeHelper(root.left);
        int rightHeight = diameterOfBinaryTreeHelper(root.right);
        diameter = Math.max(leftHeight+rightHeight, diameter);

        return Math.max(leftHeight,rightHeight) + 1;

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

        System.out.println(diameterOfBinaryTree(node1));

    }

}
