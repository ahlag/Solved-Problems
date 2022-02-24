public class SwapPairs {

    public static ListNode swapPairsRecursive(ListNode head) {

        if ((head == null) || (head.next == null) ) {
            return head;
        }

        ListNode currentNode = head;
        ListNode nextNode = head.next;

        currentNode.next = swapPairsRecursive(nextNode.next);
        nextNode.next = currentNode;

        return nextNode;
    }

    public static ListNode swapPairsIterative(ListNode head) {

        ListNode dummy = new ListNode(-1);
        dummy.next = head;

        ListNode prevNode = dummy;

        while ((head != null) && (head.next != null)) {

            ListNode currentNode = head;
            ListNode nextNode = head.next;

            prevNode.next = nextNode;
            currentNode.next = nextNode.next;
            nextNode.next = currentNode;

            prevNode = currentNode;
            head = currentNode.next;

        }

        return dummy.next;
    }

    public static void main(String[] args) {

        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
        ListNode node4 = new ListNode(4);

        node1.next = node2;
        node2.next = node3;
        node3.next = node4;

        ListNode head = swapPairsRecursive(node1);

        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }

    }
}
