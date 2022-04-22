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
        ListNode *detectCycle(ListNode *head) {
            ListNode *slow = head, *fast = head;
            while (fast && fast->next) {
                slow = slow->next;
                fast = fast->next->next;
                if (slow == fast) break;
            }
            if (!(fast && fast->next)) return NULL;
            while (head != slow) {
                head = head->next;
                slow = slow->next;
            }
            return head;
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
    node4.next = &node1;

    ListNode * res = solution.detectCycle(&node1);

    cout << res->val << endl;

    return 0;
}