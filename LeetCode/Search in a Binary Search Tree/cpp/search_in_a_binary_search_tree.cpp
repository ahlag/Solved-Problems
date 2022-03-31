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
    public:
        TreeNode* searchBST(TreeNode* root, int val) {
        if(!root)
            return nullptr;
        if(root->val == val)return root;
        else if(root->val > val) return searchBST(root->left,val);
        else return searchBST(root->right,val);
    }

    TreeNode* searchBSTIterative(TreeNode* root, int val) {
        while (root != nullptr && root->val != val) {
            root = (root->val > val) ? root->left : root->right;
        }
        return root;
    }

    void findFullNode(TreeNode* root) {
        if (root != NULL) {
            findFullNode(root->left);
            cout << root->val << " ";
            findFullNode(root->right);
        }
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

    int val = 2;
    TreeNode* res = solution.searchBST(&node1, val);

    solution.findFullNode(res);

    cout << endl;

    TreeNode* res2 = solution.searchBSTIterative(&node1, val);

    solution.findFullNode(res2);

    return 0;
}