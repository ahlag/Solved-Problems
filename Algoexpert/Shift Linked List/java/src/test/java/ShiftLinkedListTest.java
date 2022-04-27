import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class ShiftLinkedListTest {

    public List<Integer> linkedListToArray(LinkedList head) {
        var array = new ArrayList<Integer>();
        var current = head;
        while (current != null) {
            array.add(current.value);
            current = current.next;
        }
        return array;
    }

    @Test
    public void TestCase1() {
        var head = new LinkedList(0);
        head.next = new LinkedList(1);
        head.next.next = new LinkedList(2);
        head.next.next.next = new LinkedList(3);
        head.next.next.next.next = new LinkedList(4);
        head.next.next.next.next.next = new LinkedList(5);
        var result = ShiftLinkedList.shiftLinkedList(head, 2);
        var array = this.linkedListToArray(result);

        var expected = Arrays.asList(new Integer[] {4, 5, 0, 1, 2, 3});
        assertTrue(expected.equals(array));
    }

}