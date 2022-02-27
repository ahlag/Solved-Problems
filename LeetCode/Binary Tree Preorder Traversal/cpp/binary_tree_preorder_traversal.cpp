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
    vector<int> preOrder;
    vector<int> res;
    
public:
    vector<int> preorderTraversalIterative(TreeNode *root) {
        stack<TreeNode*> nodes;
        
        if(root == NULL) //in case the input is empty
            return preOrder;
        
        nodes.push(root);
        
        while(!nodes.empty()){
            TreeNode *tmpNode = nodes.top();
            
            //psuh the root's value into a vector
            preOrder.push_back(tmpNode -> val);
            
            nodes.pop();//pop the tmpNode from stack
            
            //because statk is LIFO, the right node is latter than left node
            if(tmpNode -> right != NULL)    nodes.push(tmpNode -> right);
            if(tmpNode -> left  != NULL)    nodes.push(tmpNode -> left);
        }
        
        return preOrder;
    }

    void preorderTraversalRecursiveHelper(TreeNode* root, vector<int> &res) {
        if(root) {
            res.push_back(root->val);           

            if(root->left)
                preorderTraversalRecursiveHelper(root->left, res);

            if(root->right)
                preorderTraversalRecursiveHelper(root->right, res);
        }

        return;
    }

    vector<int> preorderTraversalRecursive(TreeNode* root) {   
        preorderTraversalRecursiveHelper(root, res) ;
        return res;
    }

};

int main() {

    // Make the nodes
    TreeNode node1(1);
    TreeNode node2(2);
    TreeNode node3(3);
    
    // Connect nodes
    node1.right = &node2;
    node2.left = &node3;

    Solution solution;
    vector<int> result1 = solution.preorderTraversalIterative(&node1);

    for(auto res: result1) {
        cout << res << endl;
    }

    vector<int> result2 = solution.preorderTraversalRecursive(&node1);

    for(auto res: result2) {
        cout << res << endl;
    }

    return 0;
}