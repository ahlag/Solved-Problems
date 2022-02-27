import java.util.LinkedList;
import java.util.List;

public class BinaryTreePreOrderTraversal {

    public static List<Integer> InOrderTraversalIterative (TreeNode root) {

        LinkedList<Integer> result = new LinkedList();
        LinkedList<TreeNode> stack = new LinkedList();

        stack.add(root);

        if (root == null) {
            return result;
        }

        while(!stack.isEmpty()) {

            TreeNode node = stack.pollLast();

            result.add(node.val);

            if(node.left != null) {
                stack.add(node.left);
            }

            if(node.right != null) {
                stack.add(node.right);
            }

        }

        return result;
    }

    // Instantiate LinkedList every recursive call
    public static List<Integer> InOrderTraversalRecursive (TreeNode root) {

        List<Integer> result = new LinkedList<Integer>();
        if (root != null){
            result.add(root.val);
            result.addAll(InOrderTraversalRecursive(root.left));
            result.addAll(InOrderTraversalRecursive(root.right));
        }
        return result;
    }

    // Instantiate LinkedList Once
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> pre = new LinkedList<Integer>();
        preHelper(root,pre);
        return pre;
    }

    public void preHelper(TreeNode root, List<Integer> pre) {
        if(root==null) return;
        pre.add(root.val);
        preHelper(root.left,pre);
        preHelper(root.right,pre);
    }

    public static void main(String[] args) {

        TreeNode node1 = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);

        node1.right = node2;
        node2.left = node3;

        List<Integer> result = InOrderTraversalIterative(node1);

        for (Integer nodeVal : result) {
            System.out.println(nodeVal);
        }

        node1 = new TreeNode(1);
        node2 = new TreeNode(2);
        node3 = new TreeNode(3);

        node1.right = node2;
        node2.left = node3;

        List<Integer> result2 = InOrderTraversalRecursive(node1);

        for (Integer nodeVal : result2) {
            System.out.println(nodeVal);
        }

    }

}
