import random

from node import Node

def find_kth_from_behind(head: Node, k: int):
    curr = head
    list_len = 0
    while curr:
        list_len += 1
        curr = curr.next
    print(f"list len: {list_len}")
    target = list_len - k
    print(f"target: {target}")
    curr = head
    while target > 0:
        curr = curr.next
        target -= 1
    return curr.val


def find_kth_from_behind_v2(head: Node, k: int):

    ptr1 = head
    while k > 0:
        k -= 1
        ptr1 = ptr1.next
    print(f"ptr1: {ptr1.val}")
    ptr2 = head
    while ptr1:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr2.val


if __name__ == "__main__":
    head = Node(random.randrange(1, 50))
    curr = head

    for i in range(1, 15):
        node = Node(random.randrange(1, 50))
        curr.next = node
        curr = curr.next

    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

    ans1 = find_kth_from_behind(head, 5)
    ans2 = find_kth_from_behind_v2(head, 5)
    print(ans1, ans2)
