public class ValidateBST {

    public static boolean validateBst(BST tree) {
        return validateBstHelper(tree, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    public static boolean validateBstHelper(BST tree, int minValue, int maxValue) {

        if (tree.value <  minValue || tree.value >= maxValue) {
            return false;
        }

        if (tree.left != null && !validateBstHelper(tree.left, minValue, tree.value)) {
            return false;
        }

        if (tree.right != null && !validateBstHelper(tree.right, tree.value, maxValue)) {
            return false;
        }

        return true;
    }

    public static void main(String[] args) {

        BST root = new BST(10);
        root.left = new BST(5);
        root.left.left = new BST(2);
        root.left.left.left = new BST(1);
        root.left.right = new BST(5);
        root.right = new BST(15);
        root.right.left = new BST(13);
        root.right.left.right = new BST(14);
        root.right.right = new BST(22);

        System.out.println(validateBst(root));
    }

}
