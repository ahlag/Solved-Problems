import sun.awt.image.ImageWatched;

public class RemoveKthNodeFromEnd {

    public static void removeKthNodeFromEnd(LinkedList head, int k) {
        int counter = 1;
        LinkedList first = head;
        LinkedList second = head;
        while (counter <= k) {
            second = second.next;
            counter++;
        }
        if (second == null) {
            head.value = head.next.value;
            head.next = head.next.next;
            return;
        }
        while (second.next != null) {
            second = second.next;
            first = first.next;
        }
        first.next = first.next.next;
    }

}
