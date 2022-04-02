public class RemoveDupsRunner {

    public static void deleteDupsRunner(LinkedListNode head) {

        LinkedListNode current = head;
        while (current != null) {
            LinkedListNode runner = current;
            /* Remove all future nodes that have the same value */
            while(runner.next!=null) {
                if (runner.next.data == current.data) {
                    runner.next = runner.next.next;
                } else {
                    runner = runner.next;
                }
            }
            current = current.next;
        }
    }

    public static void main(String[] args) {
        LinkedListNode first = new LinkedListNode(0, null, null);
        LinkedListNode head = first;
        LinkedListNode second = first;
        for (int i = 1; i < 8; i++) {
            second = new LinkedListNode(i % 2, null, null);
            first.setNext(second);
            second.setPrevious(first);
            first = second;
        }
        System.out.println(head.printForward());
        deleteDupsRunner(head);
        System.out.println(head.printForward());
    }
}
