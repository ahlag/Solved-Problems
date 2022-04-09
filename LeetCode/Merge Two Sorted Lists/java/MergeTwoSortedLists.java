public class MergeTwoSortedLists {

    public ListNode mergeTwoListsIteration(ListNode list1, ListNode list2) {

        ListNode sentinel = new ListNode(-1);
        ListNode pre = sentinel;

        while (list1 != null && list2 != null) {

            if (list1.val > list2.val) {
                pre.next = list2;
                list2 = list2.next;
            } else {
                pre.next = list1;
                list1 = list1.next;
            }

            pre = pre.next;
        }

        pre.next = list1 == null ? list2 : list1;

        return sentinel.next;
    }

    public static ListNode mergeTwoListsRecursive(ListNode list1, ListNode list2) {

        if (list1 == null) {
            return list2;
        } else if (list2==null) {
            return list1;
        } else if (list1.val > list2.val) {
            list2.next = mergeTwoListsRecursive(list1, list2.next);
            return list2;
        } else {
            list1.next = mergeTwoListsRecursive(list1.next, list2);
            return list1;
        }
    }

    public static void main(String[] args) {
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
        ListNode node4 = new ListNode(4);
        ListNode node5 = new ListNode(4);
        ListNode node6 = new ListNode(5);

        node1.next = node2;
        node2.next = node4;
        node4.next = node6;
        node3.next = node5;
        ListNode printHead = node1;
        mergeTwoListsRecursive(node1, node3);

        while(printHead!=null) {
            System.out.println(printHead.val);
            printHead = printHead.next;
        }
    }

}
