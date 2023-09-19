from node import Node


def add(ptr1: Node, ptr2: Node):
    carry = 0
    result, head = None, None
    while ptr1 and ptr2:
        if result == None:
            result = Node(0)
            head = result
        else:
            result.next = Node(0)
            result = result.next
        if ptr1.val + ptr2.val + carry >= 10:
            result.val = ptr1.val + ptr2.val + carry - 10
            carry = 1
        else:
            result.val = ptr1.val + ptr2.val + carry
            carry = 0
        ptr1, ptr2 = ptr1.next, ptr2.next

    while ptr1:
        result.next = Node(0)
        result = result.next
        if ptr1.val + carry >= 10:
            result.val = ptr1.val + carry - 10
            carry = 1
        else:
            result.val = ptr1.val + carry
            carry = 0
        ptr1 = ptr1.next

    while ptr2:
        result.next = Node(0)
        result = result.next
        if ptr2.val + carry >= 10:
            result.val = ptr2.val + carry - 10
            carry = 1
        else:
            result.val = ptr2.val + carry
            carry = 0
        ptr2 = ptr2.next

    # 9->7->8, 6->8->5
    if carry == 1:
        result.next = Node(1)

    return head


if __name__ == "__main__":
    ptr1 = Node(9)
    curr = ptr1

    for num in [7, 8]:
        node = Node(num)
        curr.next = node
        curr = curr.next

    curr = ptr1
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

    ptr2 = Node(6)
    curr = ptr2

    for num in [8, 5]:
        node = Node(num)
        curr.next = node
        curr = curr.next

    curr = ptr2
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

    ptr = add(ptr1=ptr1, ptr2=ptr2)

    print()
    curr = ptr
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()
