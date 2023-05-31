import random


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


# O(n): Iterate entire linked list (twice, O(2n) to be precise)
def delete_duplicates(head: Node):
    curr = head
    hash_table = dict()
    while curr:
        if curr.val not in hash_table.keys():
            hash_table[curr.val] = 0
        curr = curr.next

    curr = head
    while curr:
        if hash_table[curr.val] == 1:
            curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
        else:
            hash_table[curr.val] += 1
        curr = curr.next

    return head


# Without additional space: O(n^2) instead
def delete_duplicates_2(head: Node):
    if head.next is None:
        return head
    ptr1 = head
    while ptr1:
        ptr2 = ptr1.next
        target = ptr1.val
        while ptr2:
            if target == ptr2.val:
                ptr2.prev.next = ptr2.next
                if ptr2.next:
                    ptr2.next.prev = ptr2.prev
            ptr2 = ptr2.next
        ptr1 = ptr1.next

    return head


if __name__ == "__main__":
    head = Node(random.randrange(1, 10))
    curr = head

    for i in range(1, 15):
        node = Node(random.randrange(1, 10))
        curr.next = node
        node.prev = curr
        curr = curr.next

    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

    head = delete_duplicates(head=head)

    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

    ################################

    head = Node(random.randrange(1, 10))
    curr = head

    for i in range(1, 15):
        node = Node(random.randrange(1, 10))
        curr.next = node
        node.prev = curr
        curr = curr.next

    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

    head = delete_duplicates_2(head=head)

    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()
