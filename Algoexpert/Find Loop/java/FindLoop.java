public class FindLoop {

    public static LinkedList findLoop(LinkedList head) {

        LinkedList first = head.next;
        LinkedList second = head.next.next;

        while(first != second) {
            first = first.next;
            second = second.next.next;
        }
        first = head;
        while(first != second) {
            first = first.next;
            second = second.next;
        }
        return first;

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
        node6.next = node3;

        LinkedList res = findLoop(node1);

        System.out.println(res.val);
    }

}
