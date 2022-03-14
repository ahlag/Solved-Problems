#include <bits/stdc++.h>

using namespace std;

class LinkedList {
public:
    int value;
    LinkedList *next = nullptr;

    LinkedList(int value) { this->value = value; }
};

LinkedList *addMany(LinkedList *linkedList, vector<int> values) {
    auto current = linkedList;
    while (current->next != nullptr) {
        current = current->next;
    }
    for (int value : values) {
        current->next = new LinkedList(value);
        current = current->next;
    }
    return linkedList;
}

vector<int> getNodesInArray(LinkedList *linkedList) {
    vector<int> nodes;
    auto current = linkedList;
    while (current != nullptr) {
        nodes.push_back(current->value);
        current = current->next;
    }
    return nodes;
}

class Solution {
    public:
        LinkedList *sumOfLinkedLists(LinkedList *linkedListOne,
                             LinkedList *linkedListTwo) {
            auto newLinkedListHeadPointer = new LinkedList(0);
            auto currentNode = newLinkedListHeadPointer;
            int carry = 0;

            auto nodeOne = linkedListOne;
            auto nodeTwo = linkedListTwo;

            while(nodeOne != nullptr || nodeTwo != nullptr || carry != 0) {

                int valueOne = nodeOne != nullptr ? nodeOne->value : 0;
                int valueTwo = nodeTwo != nullptr ? nodeTwo->value : 0;
                int sumOfValues = valueOne + valueTwo + carry;

                int newValue = sumOfValues % 10;
                auto newNode = new LinkedList(newValue);
                currentNode->next = newNode;
                currentNode = currentNode->next;

                carry = sumOfValues / 10;
                nodeOne = nodeOne != nullptr ? nodeOne->next : nullptr;
                nodeTwo = nodeTwo != nullptr ? nodeTwo->next : nullptr;
            }

            return newLinkedListHeadPointer->next;
        }

};


int main() {

    Solution solution;
    auto ll1 = addMany(new LinkedList(2), {4, 7, 1});
    auto ll2 = addMany(new LinkedList(9), {4, 5});

    auto result = solution.sumOfLinkedLists(ll1, ll2);

    for(auto res : getNodesInArray(result) ) {
        cout << res << endl;
    }

    return 0;
}