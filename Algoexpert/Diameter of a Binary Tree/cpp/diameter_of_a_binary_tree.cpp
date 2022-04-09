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
    int ans=0;

    int height(TreeNode* root) {
        if(!root) return 0;
        
        int lHeight = height(root->left);
        int rHeight = height(root->right);
        
        ans= max(ans, 1 + lHeight + rHeight);
        return 1+ max( lHeight , rHeight);

    }

    int diameterOfBinaryTree(TreeNode* root) {
        if(!root) return 0;
        height(root);
        return ans-1;
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

    cout << solution.diameterOfBinaryTree(&node1) << endl;

    return 0;
}