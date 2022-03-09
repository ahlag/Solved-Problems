import java.util.ArrayList;

public class FindKthLargestValueInBST {

    public static int findKthLargestValueInBstRecursion(BST tree, int k) {
        ArrayList<Integer> sortedNodeValues = new ArrayList<>();
        inOrderTraverse(tree, sortedNodeValues);
        return sortedNodeValues.get(sortedNodeValues.size() - k);
    }

    public static void inOrderTraverse(BST node, ArrayList<Integer> sortedNodeValues) {

        if (node == null) {
            return;
        }

        inOrderTraverse(node.left, sortedNodeValues);
        sortedNodeValues.add(node.value);
        inOrderTraverse(node.right, sortedNodeValues);

    }

    public static int findKthLargestValueInBstReverse(BST tree, int k) {
        TreeInfo treeInfo = new TreeInfo(0, -1);
        reverseInOrderTraverse(tree, k, treeInfo);
        return treeInfo.latestVisitedNodeValue;
    }

    public static void reverseInOrderTraverse(BST node, int k, TreeInfo treeInfo) {
        if (node == null || treeInfo.numberOfNodesVisited >= k) {
            return;
        }

        reverseInOrderTraverse(node.right, k, treeInfo);

        if (treeInfo.numberOfNodesVisited < k) {
            treeInfo.numberOfNodesVisited++;
            treeInfo.latestVisitedNodeValue = node.value;
            reverseInOrderTraverse(node.left, k, treeInfo);
        }
    }

    public static void main(String[] args) {
        BST root = new BST(15);
        root.left = new BST(5);
        root.left.left = new BST(2);
        root.left.left.left = new BST(1);
        root.left.left.right = new BST(3);
        root.left.right = new BST(5);
        root.right = new BST(20);
        root.right.left = new BST(17);
        root.right.right = new BST(22);
        int k = 3;

        System.out.println(findKthLargestValueInBstRecursion(root, k));
        System.out.println(findKthLargestValueInBstReverse(root, k));
    }

}
