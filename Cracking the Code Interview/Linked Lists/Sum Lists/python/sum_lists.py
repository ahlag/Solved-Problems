import time
from linkedlist import LinkedList

def sum_lists(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = NumericLinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(result % 10)
        carry = result // 10

    if carry:
        ll.add(carry)

    return ll

class NumericLinkedList(LinkedList):
    @classmethod
    def generate_from_integer(cls, integer):
        integer_parts = [int(c) for c in str(integer)]
        integer_parts.reverse()
        return cls(integer_parts)

    def numeric_value(self):
        number = 0
        for place, node in enumerate(self):
            number += node.value * 10 ** place
        return number


test_cases = (
    # all values can either be list of integer or integers
    # a, b, expected_sum
    ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
    (0, 0, 0),
    ([], [], 0),
    ([3, 2, 1], [3, 2, 1], [6, 4, 2]),
    (123, 123, 246),
    (123, 1, 124),
    (1, 123, 124),
)

testable_functions = (
    sum_lists
)

def test_numeric_linked_list():
    ll = NumericLinkedList.generate_from_integer(321)
    assert ll.numeric_value() == 321


def test_linked_list_addition():
    for f in testable_functions:
        for a, b, expected in test_cases:
            print(f"{f.__name__}: {a}, {b}, {expected}")
            if isinstance(a, int):
                ll_a = NumericLinkedList.generate_from_integer(a)
            else:
                ll_a = NumericLinkedList(a.copy())

            if isinstance(b, int):
                ll_b = NumericLinkedList.generate_from_integer(b)
            else:
                ll_b = NumericLinkedList(b.copy())
            result = f(ll_a, ll_b)
            if isinstance(expected, int):
                assert result.numeric_value() == expected
            else:
                assert result.values() == expected

def example():
    ll_a = LinkedList.generate(4, 0, 9)
    ll_b = LinkedList.generate(3, 0, 9)
    print(ll_a)
    print(ll_b)
    print(sum_lists(ll_a, ll_b))

if __name__ == "__main__":
    example()
