#include <bits/stdc++.h>

using namespace std;

class BST {
    public:
        int value;
        BST *left;
        BST *right;

        BST(int val) {
            value = val;
            left = nullptr;
            right = nullptr;
        }
};

class Solution {
    public:
        bool validateBst(BST *tree) {
            return validateBSTHelper(tree, INT_MIN, INT_MAX);
        }

        bool validateBSTHelper(BST *tree, int minValue, int maxValue) {
            
            if (tree->value < minValue || tree->value >= maxValue) {
                return false;
            }
            
            if(tree->left != nullptr && !validateBSTHelper(tree->left, minValue, tree->value)) {
                return false;
            }
                
            if(tree->right != nullptr && !validateBSTHelper(tree->right, tree->value, maxValue)) {
                return false;
            }
            
            return true;
        }
};


int main() {

    BST *root = new BST(10);
    root->left = new BST(5);
    root->left->left = new BST(2);
    root->left->left->left = new BST(1);
    root->left->right = new BST(5);
    root->right = new BST(15);
    root->right->left = new BST(13);
    root->right->left->right = new BST(14);
    root->right->right = new BST(22);

    Solution solution;
    cout <<  solution.validateBst(root) << endl;

    return 0;
}