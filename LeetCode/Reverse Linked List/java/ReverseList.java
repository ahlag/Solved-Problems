public class ReverseList {

    public ListNode reverseListRecrusive(ListNode head) {

        if (head == null || head.next == null) {
            return head;
        }

        ListNode p = reverseListRecrusive(head.next);
        head.next.next = head;
        head.next = null;

        return p;
    }

    public static ListNode reverseListIterative(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }

    public static void main(String[] args) {
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
        ListNode node4 = new ListNode(4);

        node1.next = node2;
        node2.next = node3;
        node3.next = node4;

        reverseListIterative(node1);
        ListNode cur = node4;
        while(cur != null) {
            System.out.println(cur.val);
            cur = cur.next;
        }

    }

}
