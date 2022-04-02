import java.util.ArrayList;

public class SumOfLinkedLists {

    public static LinkedList addMany(LinkedList linkedList, int[] values) {
        var current = linkedList;
        while (current.next != null) {
            current = current.next;
        }
        for (var value : values) {
            current.next = new LinkedList(value);
            current = current.next;
        }
        return linkedList;
    }

    public static ArrayList<Integer> getNodesInArray(LinkedList linkedList) {
        ArrayList<Integer> nodeValues = new ArrayList<Integer>();
        LinkedList current = linkedList;
        while (current != null) {
            nodeValues.add(current.value);
            current = current.next;
        }
        return nodeValues;
    }

    public static LinkedList sumOfLinkedListsLoop(LinkedList linkedListOne, LinkedList linkedListTwo) {
        LinkedList newLinkedListHeadPointer = new LinkedList(0);
        LinkedList currentNode = newLinkedListHeadPointer;
        int carry = 0;

        LinkedList nodeOne = linkedListOne;
        LinkedList nodeTwo = linkedListTwo;

        while(nodeOne != null || nodeTwo != null || carry != 0) {

            int valueOne = nodeOne != null ? nodeOne.value : 0;
            int valueTwo = nodeTwo != null ? nodeTwo.value : 0;
            int sumOfValues = valueOne + valueTwo + carry;

            int newValue = sumOfValues % 10;
            LinkedList newNode = new LinkedList(newValue);
            currentNode.next = newNode;
            currentNode = currentNode.next;

            carry = sumOfValues / 10;
            nodeOne = nodeOne != null ? nodeOne.next : null;
            nodeTwo = nodeTwo != null ? nodeTwo.next : null;
        }

        return newLinkedListHeadPointer.next;
    }

    public static void main(String[] args) {
        LinkedList ll1 = addMany(new LinkedList(2), new int[] {4, 7, 1});
        LinkedList ll2 = addMany(new LinkedList(9), new int[] {4, 5});
        LinkedList actual = sumOfLinkedListsLoop(ll1, ll2);
        ArrayList result = getNodesInArray(actual);

        // For loop
        for (Object integer : result) {
            System.out.println(integer);
        }

        // Functional
        result.stream().forEach(System.out::println);
    }
}
