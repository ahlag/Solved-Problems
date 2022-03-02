#include <bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
    public:

    // Floyd Algorithm
    bool hasCycleFloyd(ListNode *head) {
        if (!head) 
            return false;
        
        ListNode *slow = head, *fast = head;
        
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) 
                return true;
        }
        
        return false;
    }

    //hashmap approach
    bool hasCycleHashMap(ListNode *head) {

        if(head==NULL)
            return false;

        unordered_map<ListNode*,int> map;

        while(head!=NULL){
            if(map.count(head)>0)
                return true;
            else
                map[head]=1;
            head=head->next;
        }

        return false;
    }


};


int main() {

    ListNode node1 = ListNode(3);
    ListNode node2 = ListNode(2);
    ListNode node3 = ListNode(0);
    ListNode node4 = ListNode(-4);

    node1.next = &node2;
    node2.next = &node3;
    node3.next = &node4;
    node4.next = &node2;

    Solution solution;

    cout << solution.hasCycleFloyd(&node1) << endl;

    return 0;
}