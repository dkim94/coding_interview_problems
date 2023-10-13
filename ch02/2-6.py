from node import Node

def is_palindrome(head: Node):
    stack = []
    curr = head
    while curr:
        stack.append(curr.val)
        curr = curr.next
    curr = head
    while curr:

        if curr.val != stack.pop():
            return False
        curr = curr.next
    return True

if __name__ == "__main__":
    head = Node(9)
    curr = head

    for num in [7, 8, 7, 9]:
        node = Node(num)
        curr.next = node
        curr = curr.next

    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

    print(is_palindrome(head=head))