#include <bits/stdc++.h>

using namespace std;

class LinkedList {
    public:
        int value;
        LinkedList *next;

        LinkedList(int value);
};

LinkedList::LinkedList(int value) {
    this->value = value;
    this->next = nullptr;
}

LinkedList *findLoop(LinkedList *head) {

    LinkedList *first = head->next;
    LinkedList *second = head->next->next;
    while (first != second) {
        first = first->next;
        second = second->next->next;
    }
    first = head;
    while (first != second) {
        first = first->next;
        second = second->next;
    }

    return first;
}

void addMany(LinkedList *ll, vector<int> values) {
    LinkedList *current = ll;
    while (current->next != nullptr) {
        current = current->next;
    }
    for (int value : values) {
        current->next = new LinkedList(value);
        current = current->next;
    }
}

LinkedList *getNthNode(LinkedList *ll, int n) {
    int counter = 1;
    LinkedList *current = ll;
    while (counter < n) {
        current = current->next;
        counter++;
    }
    return current;
}

int main() {

    LinkedList test(0);
    addMany(&test, {1, 2, 3, 4, 5, 6, 7, 8, 9});
    getNthNode(&test, 10)->next = getNthNode(&test, 5);
    assert(findLoop(&test) == getNthNode(&test, 5));

    return 0;
}
