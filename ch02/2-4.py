import random

from node import Node


def partition(head: Node, target: int):
    dummy = Node(0)
    dummy.next = head

    ptr1, ptr2 = head, dummy
    while ptr1:
        if ptr1.val < target:
            ptr2 = ptr2.next
            ptr1.val, ptr2.val = ptr2.val, ptr1.val
        ptr1 = ptr1.next


if __name__ == "__main__":
    head = Node(3)
    curr = head

    for num in [5, 8, 5, 10, 2, 1]:
        node = Node(num)
        curr.next = node
        curr = curr.next

    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()


    partition(head, target=5)

    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()
