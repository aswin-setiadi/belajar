#!/bin/python3
# https://www.youtube.com/watch?v=HqPJF2L5h9U
from collections import deque


class Node(object):
    def __init__(self, k: int) -> None:
        self.key = k
        self.left: Node | None = None
        self.right: Node | None = None
        self.parent: Node | None = None


class FailNodeInsertionException(Exception):
    ...


class MaxHeap:
    """
    max heap is when all descendants is smaller than current node
    must keep heap complete
    say we have full heap with 3 level complete heap, we insert from
    node 8 (bottomest leftest), and compare with parent and swap if larger
    until it is smaller than parent / reached root

    in heap, only root element is deleted, then the bottomest rightest
    will go to root, then check between left and right child which 1 bigger
    and swap it with root if root< the child, then repeat with grandchilds
    against child until leaf level or until the node > its both children

    both insert and delete runtime is O(1) to O(log n)

    heap creation is similar to insertion, just start from root and
    to node 2, 3, 4, 5, ... and so on

    creating heap is n log n, deleting heap is n log n
    both will result in a sorted array of values
    so sorting the heap is 2 * nlog n ~ nlog n

    heapify (O of n according to Abdul Bari) sort the heap so each parent
    is bigger than its descendants

    it first check bottomestest right node and check its descendants
    if descendant/ descendats are bigger, swap with the biggest, then repeat
    for the node it swap until cant swap anymore/ at leaf
    then slowly repeat the check to the left,
    and go to top and left, and so on

    Heap properties
    - is a complete binary tree
    - can have duplicate

    to reverse min/ max, just multiply number by -1
    """

    def __init__(self, k: int) -> None:
        self.root = Node(k)

    def insert(self, k: int) -> None:
        def sort_after_insert(n: Node):
            if n.parent is not None:
                if n.key > n.parent.key:
                    tmp = n.key
                    n.key = n.parent.key
                    n.parent.key = tmp
                    sort_after_insert(n.parent)

        n = self.find_node_to_insert()
        if n is None:
            raise FailNodeInsertionException
        else:
            if n.left is None:
                n.left = Node(k)
                n.left.parent = n
                sort_after_insert(n.left)
            elif n.right is None:
                n.right = Node(k)
                n.right.parent = n
                sort_after_insert(n.right)
            else:
                raise FailNodeInsertionException

    def find_node_to_insert(self) -> None | Node:
        q: deque[Node] = deque([self.root])
        n: None | Node = None
        while q:
            n = q.pop()
            if n.left is None:
                break
            else:
                q.appendleft(n.left)

            if n.right is None:
                break
            else:
                q.appendleft(n.right)
        return n

    def traverse_heap(self):
        q: deque[Node] = deque([self.root])
        l: list[int] = []
        while q:
            n = q.pop()
            l.append(n.key)
            if n.left is not None:
                q.appendleft(n.left)
            if n.right is not None:
                q.appendleft(n.right)
        print(l)
        return l


def main():
    mh = MaxHeap(0)
    mh.insert(10)
    mh.insert(20)
    mh.insert(30)
    mh.insert(40)
    mh.insert(50)
    mh.insert(60)
    mh.traverse_heap()  # [60, 30, 50, 0, 20, 10, 40]


if __name__ == "__main__":
    main()
