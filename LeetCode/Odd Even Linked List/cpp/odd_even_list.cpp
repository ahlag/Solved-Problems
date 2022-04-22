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
        ListNode* oddEvenList(ListNode* head) {
            if(!head || !head->next || !head->next->next) return head;
            
            ListNode *odd = head;
            ListNode *even = head->next;
            ListNode *even_start = head->next;
            
            while(odd->next && even->next){
                odd->next = even->next; //Connect all odds
                even->next = odd->next->next;  //Connect all evens
                odd = odd->next;
                even = even->next;
            }
            odd->next = even_start;   //Place the first even node after the last odd node.
            return head; 
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
    ListNode node5 = ListNode{5};

    node1.next = &node2;
    node2.next = &node3;
    node3.next = &node4;
    node4.next = &node5;

    solution.oddEvenList(&node1);
    solution.printLinkedList(&node1);

    return 0;
}