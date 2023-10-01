class Node:
    """
    https://www.geeksforgeeks.org/data-structures/linked-list/doubly-linked-list/
    doubly linked list can be implemented with xor
    a -> b, b XOR c -> a

    """

    def __init__(self, previous, next, data) -> None:
        self.previous = previous
        self.next = next
        self.data = data
