# Implement stack with linked list


class StackNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.min_val = None


class Stack:
    def __init__(self) -> None:
        self.head = None

    def print(self):
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()

    def push(self, node: StackNode):
        if self.head is None:
            node.min_val = node.val
            self.head = node
            return
        elif self.head.min_val > node.val:
            node.min_val = node.val
        else:
            node.min_val = self.head.min_val
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            return
        else:
            val = self.head.val
            self.head = self.head.next
            return val

    def min(self):
        return self.head.min_val


if __name__ == "__main__":
    stack = Stack()
    ls = [StackNode(2), StackNode(4), StackNode(5), StackNode(1), StackNode(7)]
    for node in ls:
        stack.push(node=node)

    assert stack.min() == 1

    stack.print()

    stack.pop()
    stack.pop()

    stack.print()

    assert stack.min() == 2
