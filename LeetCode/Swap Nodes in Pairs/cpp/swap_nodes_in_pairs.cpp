#include <bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
    public:
    ListNode* swapPairsIterative(ListNode *head) {
        
        if(!head || !head->next) return head; //If there are less than 2 nodes in the given nodes, then no need to do anything just return the list as it is.
		
        ListNode* dummyNode = new ListNode(-1);
        
        ListNode* prevNode=dummyNode;
        ListNode* currNode=head;
        
        while(currNode && currNode->next){
            prevNode->next = currNode->next;
            currNode->next = prevNode->next->next;
            prevNode->next->next = currNode;
            
            prevNode = currNode;
            currNode = currNode->next;
        }
        
        return dummyNode->next;
    }

    ListNode* swapPairsRecursive(ListNode* head){

        // if head is NULL OR just having a single node, then no need to change anything 
        if(head == NULL || head->next == NULL) return head;
            
        ListNode* temp; // temporary pointer to store head -> next
        temp = head->next; // give temp what he want
        
        head->next = swapPairsRecursive(head->next->next); // changing links
        temp->next = head; // put temp -> next to head
        
        return temp; // now after changing links, temp act as our head
    }

        ListNode* swapPairsRecursiveCYLik(ListNode* head){

        // if head is NULL OR just having a single node, then no need to change anything 
        if(head == NULL || head->next == NULL) return head;

        ListNode* currentNode = head;
        ListNode* nextNode = head->next; // give temp what he want
        
        currentNode->next = swapPairsRecursiveCYLik(nextNode->next);
        nextNode->next = currentNode->next;
        
        return nextNode; // now after changing links, temp act as our head
    }
    
};

int main() {

    ListNode* l = new ListNode(2);
    l->next = new ListNode(5);
    l->next->next = new ListNode(3);
    l->next->next->next = new ListNode(4);
    l->next->next->next->next = new ListNode(6);
    l->next->next->next->next->next = new ListNode(2);
    l->next->next->next->next->next->next = new ListNode(2);

    cout<<"List: "<<endl;
    ListNode* p = l;

    while(p != NULL){
        cout<<p->val<<" ";
        p = p->next;
    }
    cout << endl;

    Solution solution;
    cout<<"After swap List: "<<endl;
    p = solution.swapPairsRecursiveCYLik(l);
    while(p != NULL){
        cout<<p->val<<" ";
        p = p->next;
    }
    cout<<endl;
    return 0;
}