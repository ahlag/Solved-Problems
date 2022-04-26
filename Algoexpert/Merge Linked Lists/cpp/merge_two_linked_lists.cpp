#include <bits/stdc++.h>

using namespace std;

// This is an input class. Do not edit.
class LinkedList {
    public:
        int value;
        LinkedList *next;

        LinkedList(int value) {
            this->value = value;
            next = nullptr;
        }
};

LinkedList *addMany(LinkedList *ll, vector<int> values) {
    LinkedList *current = ll;
    while (current->next != nullptr) {
        current = current->next;
    }
    for (auto value : values) {
        current->next = new LinkedList(value);
        current = current->next;
    }
    return ll;
}

vector<int> getNodesInArray(LinkedList *ll) {
    vector<int> nodes;
    LinkedList *current = ll;
    while (current != nullptr) {
        nodes.push_back(current->value);
        current = current->next;
    }
    return nodes;
}

LinkedList *mergeLinkedLists(LinkedList *headOne, LinkedList *headTwo) {
    LinkedList *p1 = headOne;
    LinkedList *p2 = headTwo;
    LinkedList *p1Prev = nullptr;

    while(p1 != nullptr && p2 != nullptr) {
        if (p1->value < p2->value) {
            p1Prev = p1;
            p1 = p1->next;
        } else {
            if (p1Prev != nullptr) {
                p1Prev->next = p2;
            }
            p1Prev = p2;
            p2 = p2->next;
            p1Prev->next = p1;
        }
    }
    
    if (p1 == nullptr) {
        p1Prev->next = p2;
    }
    return headOne->value < headTwo->value ? headOne : headTwo;
}


int main() {

    LinkedList *list1 = new LinkedList(2);
    addMany(list1, {6, 7, 8});
    LinkedList *list2 = new LinkedList(1);
    addMany(list2, {3, 4, 5, 9, 10});
    LinkedList *output = mergeLinkedLists(list1, list2);
    vector<int> expectedNodes = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    assert(getNodesInArray(output) == expectedNodes);

    return 0;
}
