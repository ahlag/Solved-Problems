#include <bits/stdc++.h>

using namespace std;

struct Node {
    char data;
    Node * next;
    Node( char c ) : data{ c }, next{ nullptr } { }
};

/**
 * [printList - Helper routine to print the list]
 * @param head [head of the list]
 */
void printList( Node * head ) {
    while( head ) {
        cout << head->data << "-->";
        head = head->next;
    }
    cout << "nullptr" << endl;
}

/**
 * [deleteNode - delete the "node" from the list]
 * @param node [node to be deleted]
 */
void deleteNode( Node * node ) {
    if ( node == nullptr || node->next == nullptr ) {
        return;
    }
    Node * nextNode = node->next;
    node->data = nextNode->data;
    node->next = nextNode->next;
    delete nextNode;
}

int main() {
    Node * head = new Node('a');
    head->next = new Node('b');
    head->next->next = new Node('c');
    head->next->next->next = new Node('d');
    head->next->next->next->next = new Node('e');
    cout << "List before deletion:\n";
    printList(head);
    cout << "Deleting node containing data as 'c'\n";
    deleteNode(head->next->next);
    cout << "List after deletion:\n";
    printList(head);
    return 0;
}