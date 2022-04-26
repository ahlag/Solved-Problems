public class MergeLinkedLists {

    public static LinkedList mergeLinkedLists(LinkedList headOne, LinkedList headTwo) {
        LinkedList p1 = headOne;
        LinkedList p1Prev = null;
        LinkedList p2 = headTwo;
        while (p1 != null && p2 != null) {
            if(p1.val < p2.val) {
                p1Prev = p1;
                p1 = p1.next;
            } else {
                if(p1Prev != null) p1Prev.next = p2;
                p1Prev = p2;
                p2 = p2.next;
                p1Prev.next = p1;
            }
        }
        if (p1 == null) p1Prev.next = p2;
        return headOne.val < headTwo.val ? headOne : headTwo;
    }

    public static void main(String[] args) {
        LinkedList node1 = new LinkedList(1);
        LinkedList node2 = new LinkedList(2);
        LinkedList node3 = new LinkedList(3);
        LinkedList node4 = new LinkedList(4);
        LinkedList node5 = new LinkedList(5);
        LinkedList node6 = new LinkedList(6);

        node1.next = node2;
        node2.next = node3;
        node3.next = node4;
        node4.next = node5;
        node5.next = node6;

        LinkedList node7 = new LinkedList(7);
        LinkedList node8 = new LinkedList(8);

        node7.next = node8;

        LinkedList res = mergeLinkedLists(node1, node7);
        LinkedList head = res;

        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }
    }

}
