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
        ListNode* mergeTwoListsIterative(ListNode* list1, ListNode* list2) {
            // if list1 happen to be NULL
            // we will simply return list2.
            if(list1 == NULL)
                return list2;
            
            // if list2 happen to be NULL
            // we will simply return list1.
            if(list2 == NULL)
                return list1;
            
            ListNode * ptr = list1;
            if(list1 -> val > list2 -> val)
            {
                ptr = list2;
                list2 = list2 -> next;
            }
            else
            {
                list1 = list1 -> next;
            }
            ListNode *curr = ptr;
            
            // till one of the list doesn't reaches NULL
            while(list1 &&  list2)
            {
                if(list1 -> val < list2 -> val){
                    curr->next = list1;
                    list1 = list1 -> next;
                }
                else{
                    curr->next = list2;
                    list2 = list2 -> next;
                }
                curr = curr -> next;
                    
            }
            
            // adding remaining elements of bigger list.
            if(!list1)
                curr -> next = list2;
            else
                curr -> next = list1;
                
            return ptr;
        
        }

        ListNode* mergeTwoListsRecursive(ListNode* l1, ListNode* l2) {
            // if list1 happen to be NULL
            // we will simply return list2.
            if(l1 == NULL)
            {
                return l2;
            }
            
            // if list2 happen to be NULL
            // we will simply return list1.
            if(l2 == NULL)
            {
                return l1;
            } 
            
            // if value pointend by l1 pointer is less than equal to value pointed by l2 pointer
            // we wall call recursively l1 -> next and whole l2 list.
            if(l1 -> val <= l2 -> val)
            {
                l1 -> next = mergeTwoListsRecursive(l1 -> next, l2);
                return l1;
            }
            // we will call recursive l1 whole list and l2 -> next
            else
            {
                l2 -> next =mergeTwoListsRecursive(l1, l2 -> next);
                return l2;            
            }
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
    node2.next = &node5;
    node3.next = &node4;
    node5.next = &node6;
    node4.next = &node7;
    ListNode preHead = node1;
    solution.mergeTwoListsRecursive(&node1, &node3);
    solution.printLinkedList(&preHead);

    return 0;
}