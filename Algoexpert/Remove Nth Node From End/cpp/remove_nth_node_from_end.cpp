#include <bits/stdc++.h>

using namespace std;

class LinkedList {
    public:
        int value;
        LinkedList *next;

        LinkedList(int value);
        void addMany(vector<int> values);
        vector<int> getNodesInArray();
};

class TestLinkedList : public LinkedList {
public:
    TestLinkedList(int value); 
    void addMany(vector<int> values);
    vector<int> getNodesInArray();
};

LinkedList::LinkedList(int value) {
    this->value = value;
    this->next = nullptr;
}

TestLinkedList::TestLinkedList(int value) : LinkedList(value) {
    this->value = value;
    this->next = nullptr;
}

void TestLinkedList::addMany(vector<int> values) {
    LinkedList *current = this;
    while (current->next != nullptr) {
        current = current->next;
    }

    for (int value : values) {
        current->next = new LinkedList(value);
        current = current->next;
    }
}

vector<int> TestLinkedList::getNodesInArray() {
    vector<int> nodes{};
    LinkedList *current = this;
    while (current != nullptr) {
        nodes.push_back(current->value);
        current = current->next;
    }
    return nodes;
}

void removeKthNodeFromEnd(LinkedList *head, int k) {
    int counter = 1;
    LinkedList *first = head;
    LinkedList *second = head;
    while (counter <= k) {
        second = second->next;
        counter++;
    }
    if (second == nullptr) {
        head->value = head->next->value;
        head->next = head->next->next;
        return;
    }
    while (second->next != nullptr) {
        second = second->next;
        first = first->next;
    }
    first->next = first->next->next;
}

int main() {

    TestLinkedList test(0);
    test.addMany({1, 2, 3, 4, 5, 6, 7, 8, 9});
    TestLinkedList expected(0);
    expected.addMany({1, 2, 3, 4, 5, 7, 8, 9});
    removeKthNodeFromEnd(&test, 4);
    assert(test.getNodesInArray() == expected.getNodesInArray());

    return 0;
}
