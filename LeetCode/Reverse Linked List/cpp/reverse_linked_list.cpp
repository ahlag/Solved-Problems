#include <bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
    public:
        ListNode* reverseListIterative(ListNode* head) {
            ListNode *nextNode, *prevNode = NULL;
            while (head) {
                nextNode = head->next;
                head->next = prevNode;
                prevNode = head;
                head = nextNode;
            }
            return prevNode;
        }

        ListNode* reverseListRecursive(ListNode* head) {
            // base case for recursion is if head is null:
            if (head == NULL || head -> next == NULL) {
                    return head;
                }
            // recursive call so passing all elements except first because in recursion we break nodes as 1 and (n-1) and we handle 1 and recursion handles (n-1) part:
            ListNode* node = reverseListRecursive(head -> next);
            head -> next -> next = head;
            head -> next = NULL;
            return node;
        }

        void printLinkedList(ListNode* head) {

            while(head!=nullptr) {
                cout << head->val << endl;
                head = head->next;
            }

        }

};


int main() {

    Solution solution;

    ListNode node1 = ListNode{1};
    ListNode node2 = ListNode{2};
    ListNode node3 = ListNode{3};
    ListNode node4 = ListNode{4};

    node1.next = &node2;
    node2.next = &node3;
    node3.next = &node4;

    solution.reverseListIterative(&node1);
    solution.printLinkedList(&node4);

    return 0;
}