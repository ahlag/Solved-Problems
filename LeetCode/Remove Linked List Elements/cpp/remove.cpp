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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummy = new ListNode;
        dummy -> next = head;
        ListNode* curr = dummy;
        
        while(curr -> next) {
            if(curr -> next -> val == val) {
                curr -> next = curr -> next -> next;
            } else {
                curr = curr -> next;
            }
        }
        
        return dummy -> next;
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
    ListNode node4 = ListNode{3};
    ListNode node5 = ListNode{3};
    ListNode node6 = ListNode{4};
    ListNode node7 = ListNode{6};

    node1.next = &node2;
    node2.next = &node3;
    node3.next = &node4;
    node4.next = &node5;
    node5.next = &node6;
    node6.next = &node7;
    ListNode preHead = node1;
    solution.removeElements(&node1, 3);
    solution.printLinkedList(&preHead);

    return 0;
}