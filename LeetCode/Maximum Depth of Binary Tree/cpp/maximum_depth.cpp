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
    int maxDepthRecursive(TreeNode *root) {
        if (root == NULL) {
            return 0;
        }
        return max(maxDepthRecursive(root->left), maxDepthRecursive(root->right)) + 1;
    }

    int maxDepthIterative(TreeNode *root) {

        if (root == NULL) {
            return 0;
        }

        vector<pair<int, TreeNode*>> my_stack;
        my_stack.push_back(pair<int, TreeNode*>(1, root));
        int max_depth = 0;

        while(!my_stack.empty()) {
            pair<int, TreeNode*> my_pair = my_stack.back();
            int current_depth = get<0>(my_pair);
            TreeNode* current_node = get<1>(my_pair);
            max_depth = max(current_depth, max_depth);
            my_stack.pop_back();
            if (current_node->left != NULL) {
                my_stack.push_back(pair<int, TreeNode*>(current_depth+1, current_node->left));
            }

            if (current_node->right != NULL) {
                my_stack.push_back(pair<int, TreeNode*>(current_depth+1, current_node->right));
            }

        }

        return max_depth;
    }
};


int main() {

    TreeNode node1 = TreeNode(3);
    TreeNode node2 = TreeNode(9);
    TreeNode node3 = TreeNode(20);
    TreeNode node4 = TreeNode(15);
    TreeNode node5 = TreeNode(7);

    node1.left = &node2;
    node1.right = &node3;
    node3.left = &node4;
    node3.right = &node5;

    Solution solution;
    cout <<  solution.maxDepthRecursive(&node1) << endl;
    cout <<  solution.maxDepthIterative(&node1) << endl;

    return 0;
}