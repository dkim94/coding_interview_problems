class Node:
    def __init__(self, val: int) -> None:
        self.val: int= val
        self.prev: Node = None
        self.next: Node = None
