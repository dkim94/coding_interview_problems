import random

from node import Node


def delete_node(node: Node):
    curr = node
    while curr.next:
        curr.val = curr.next.val
        if curr.next.next is None:
            curr.next = None
            break
        curr = curr.next


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

    
    curr = head
    for i in range(3):
        curr = curr.next
    print(f"delete_node: {curr.val}")
    delete_node(node=curr)


    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()
