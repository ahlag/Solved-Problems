public class reverseLinkedList {

    public static LinkedList reverseLinkedList(LinkedList head) {

        LinkedList previousNode = null;
        LinkedList currentNode = head;
        while (currentNode != null) {
            LinkedList nextNode = currentNode.next;
            currentNode.next = previousNode;
            previousNode = currentNode;
            currentNode = nextNode;
        }
        return previousNode;
    }

    public static void main(String[] args) {

        LinkedList node1 = new LinkedList(1);
        LinkedList node2 = new LinkedList(2);
        LinkedList node3 = new LinkedList(3);
        LinkedList node4 = new LinkedList(4);

        node1.next = node2;
        node2.next = node3;
        node3.next = node4;

        LinkedList head = reverseLinkedList(node1);

        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }

    }

}
