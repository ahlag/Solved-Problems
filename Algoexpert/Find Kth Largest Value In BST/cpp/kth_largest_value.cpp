#include <bits/stdc++.h>

using namespace std;

class BST {
    public:
        int value;
        BST *left = nullptr;
        BST *right = nullptr;

        BST(int value) { this->value = value; }
};

struct TreeInfo {
    int numberOfNodesVisited;
    int latestVistedNodeValue;
};

class Solution {
    public:
        int findKthLargestValueInBstRecursion(BST *tree, int k) {
            vector<int> sortedNodeValues;
            inOrderTraverse(tree, sortedNodeValues);
            return sortedNodeValues[sortedNodeValues.size() - k];
        }

        void inOrderTraverse(BST *node, vector<int> &sortedNodeValues) {
            
            if (node == nullptr) {
                return;
            }

            inOrderTraverse(node->left, sortedNodeValues);
            sortedNodeValues.push_back(node->value);
            inOrderTraverse(node->right, sortedNodeValues);

        }

        int findKthLargestValueInBstReverse(BST *tree, int k) {
            auto treeInfo = TreeInfo{0, -1};
            reverseInOrderTraverse(tree, k, treeInfo);
            return treeInfo.latestVistedNodeValue;
        }

        void reverseInOrderTraverse(BST *node, int k, TreeInfo &treeInfo ) {
            
            if (node == nullptr || treeInfo.numberOfNodesVisited >= k) {
                return;
            }

            reverseInOrderTraverse(node->right, k, treeInfo);
            if(treeInfo.numberOfNodesVisited < k) {
                treeInfo.numberOfNodesVisited++;
                treeInfo.latestVistedNodeValue = node->value;
                reverseInOrderTraverse(node->left, k, treeInfo);
            }
        }
};


int main() {

    auto root = new BST(15);
    root->left = new BST(5);
    root->left->left = new BST(2);
    root->left->left->left = new BST(1);
    root->left->left->right = new BST(3);
    root->left->right = new BST(5);
    root->right = new BST(20);
    root->right->left = new BST(17);
    root->right->right = new BST(22);
    int k = 3;

    Solution solution;
    cout <<  solution.findKthLargestValueInBstRecursion(root, k) << endl;
    cout <<  solution.findKthLargestValueInBstReverse(root, k) << endl;

    return 0;
}