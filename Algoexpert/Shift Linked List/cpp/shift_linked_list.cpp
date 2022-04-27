#include <bits/stdc++.h>

using namespace std;

class LinkedList {
    public:
        int value;
        LinkedList *next;

        LinkedList(int value) {
            this->value = value;
            next = nullptr;
        }
};

vector<int> linkedListToArray(LinkedList *head) {
    vector<int> array{};
    auto current = head;
    while (current != nullptr) {
        array.push_back(current->value);
        current = current->next;
    }
    return array;
}

LinkedList *shiftLinkedList(LinkedList *head, int k) {

    int listLength = 1;
    LinkedList *listTail = head;
    while (listTail->next != nullptr) {
        listTail = listTail->next;
        listLength++;
    }

    int offset = abs(k) % listLength;
    if (offset == 0) return head;
    int newTailPosition = k > 0 ? listLength - offset : offset;
    LinkedList *newTail = head;
    for (int i = 1; i < newTailPosition; i++) {
        newTail = newTail->next;
    }
    LinkedList *newHead = newTail->next;
    newTail->next = nullptr;
    listTail->next = head;
    return newHead;
}

int main() {

    auto head = new LinkedList(0);
    head->next = new LinkedList(1);
    head->next->next = new LinkedList(2);
    head->next->next->next = new LinkedList(3);
    head->next->next->next->next = new LinkedList(4);
    head->next->next->next->next->next = new LinkedList(5);
    auto result = shiftLinkedList(head, 2);
    auto array = linkedListToArray(result);

    vector<int> expected{4, 5, 0, 1, 2, 3};
    assert(expected == array);

}
