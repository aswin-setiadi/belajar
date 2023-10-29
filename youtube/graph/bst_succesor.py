#!/bin/python3

# https://www.youtube.com/watch?v=jma9hFQSCDk

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node(object):
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None


class BST:
    """BST normally assumes there are no duplicate keys"""

    def __init__(self, k: int) -> None:
        self.root = Node(k)

    def insert(self, node: Node, k: int) -> None:
        if k < node.key:
            if node.left is None:
                node.left = Node(k, parent=node)
            else:
                self.insert(node.left, k)
        else:
            if node.right is None:
                node.right = Node(k, parent=node)
            else:
                self.insert(node.right, k)

    def find_node(self, k: int, node: Node) -> Optional[Node]:
        if node.key == k:
            return node
        if k < node.key:
            if node.left is not None:
                return self.find_node(k, node.left)
            else:
                return None
        else:
            if node.right is not None:
                return self.find_node(k, node.right)
            else:
                return None


class Solution(object):
    """find the smallest higher node key of the target"""

    @staticmethod
    def _traverse_leftmost(node: Node) -> Node:
        if node.left is not None:
            return Solution._traverse_leftmost(node.left)
        else:
            # leaf node
            return node

    @staticmethod
    def _traverse_parent(node: Node) -> Optional[Node]:
        if node.parent is None:
            return None
        child = node
        parent = node.parent
        if child == parent.left:
            # found minimum inOrder successor:
            return parent
        else:
            return Solution._traverse_parent(parent)

    @staticmethod
    def solve(node: Node) -> Node | None:
        # if right node is not None, find lowest leftmost right descendant
        if node.right is not None:
            return Solution._traverse_leftmost(node.right)
        if node.parent is None:
            # root without right branch, return None
            return None
        if node.parent.left is not None and node == node.parent.left:
            # node is left, return parent
            return node.parent
        if node.parent.right is not None and node == node.parent.right:
            # node is right, traverse parent and above
            return Solution._traverse_parent(node.parent)


def main():
    bst = BST(20)
    bst.insert(bst.root, 9)
    bst.insert(bst.root, 25)
    bst.insert(bst.root, 5)
    bst.insert(bst.root, 12)
    bst.insert(bst.root, 11)
    bst.insert(bst.root, 14)
    inputNode = bst.find_node(9, bst.root)
    if inputNode is not None:
        ans = Solution.solve(inputNode)
        if ans is not None:
            print(ans.key)
        else:
            print(ans)
    inputNode = bst.find_node(14, bst.root)
    if inputNode is not None:
        ans = Solution.solve(inputNode)
        if ans is not None:
            ans = ans.key
        print(ans)


if __name__ == "__main__":
    main()
