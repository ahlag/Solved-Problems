#include <bits/stdc++.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
private:
    stack<TreeNode*> stk, lower_limits, upper_limits;
    TreeNode* prev = nullptr;

public:
    bool validateValidRangeRecursive(TreeNode* root, TreeNode* low, TreeNode* high) {
        // Empty trees are valid BSTs.
        if (root == nullptr) {
            return true;
        }

        // The current node's value must be between low and high.
        if ((low != nullptr and root->val <= low->val) or
            (high != nullptr and root->val >= high->val)) {
            return false;
        }

        // The left and right subtree must also be valid.
        return validateValidRangeRecursive(root->right, root, high) and
                validateValidRangeRecursive(root->left, low, root);
    }

    bool isValidBSTValidRangeRecursive(TreeNode* root) {
        return validateValidRangeRecursive(root, nullptr, nullptr);
    }

    void update(TreeNode* root, TreeNode* low, TreeNode* high) {
        stk.push(root);
        lower_limits.push(low);
        upper_limits.push(high);
    }

    bool isValidBSTValidRangeIterative(TreeNode* root) {
        TreeNode* low = nullptr;
        TreeNode* high = nullptr;
        update(root, low, high);

        while (!stk.empty()) {
            root = stk.top();
            stk.pop();
            low = lower_limits.top();
            lower_limits.pop();
            high = upper_limits.top();
            upper_limits.pop();

            if (root == nullptr) {
                continue;
            }

            TreeNode* val_node = root;
            if (low != nullptr and val_node->val <= low->val) {
                return false;
            }
            if (high != nullptr and val_node->val >= high->val) {
                return false;
            }
            update(root->right, val_node, high);
            update(root->left, low, val_node);
        }
        return true;
    }

    bool isValidBSTinOrderRecursive(TreeNode* root) {
        return inOrderRecursive(root);
    }

    bool inOrderRecursive(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        if (!inOrderRecursive(root->left)) {
            return false;
        }
        if (prev != nullptr && root->val <= prev->val) {
            return false;
        }
        prev = root;
        return inOrderRecursive(root->right);
    }

    bool isValidBSTinOrderIterative(TreeNode* root) {
        stack<TreeNode*> stk;
        TreeNode* prev = nullptr;

        while (!stk.empty() or root != nullptr) {
            while (root != nullptr) {
                stk.push(root);
                root = root->left;
            }
            root = stk.top();
            stk.pop();

            // If next element in inorder traversal
            // is smaller than the previous one
            // that's not BST.
            if (prev != nullptr and root->val <= prev->val) {
                return false;
            }
            prev = root;
            root = root->right;
        }
        return true;
    }
};

int main() {

    TreeNode node1 = TreeNode(4);
    TreeNode node2 = TreeNode(2);
    TreeNode node3 = TreeNode(7);
    TreeNode node4 = TreeNode(1);
    TreeNode node5 = TreeNode(3);

    node1.left = &node2;
    node1.right = &node3;
    node2.left = &node4;
    node2.right = &node5;

    Solution solution;

    cout << solution.isValidBSTValidRangeRecursive(&node1) << endl;
    cout << solution.isValidBSTValidRangeIterative(&node1) << endl;
    cout << solution.isValidBSTinOrderRecursive(&node1) << endl;
    cout << solution.isValidBSTinOrderIterative(&node1) << endl;

    return 0;
}