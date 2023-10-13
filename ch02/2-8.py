from node import Node


def find_start_of_circular(head: Node):
    curr = head
    while curr and not curr.visited:
        curr.visited = True
        curr = curr.next

    if not curr:
        return None
    else:
        return curr
    

if __name__ == "__main__":
    head = Node(1)
    curr = head

    for i in range(2, 6):
        node = Node(i)
        curr.next = node
        curr = curr.next

    curr.next = head # circular

    start_of_circular =  find_start_of_circular(head=head)
    assert start_of_circular.val == head.val
