#!/bin/python3
# https://www.geeksforgeeks.org/sub-tree-nodes-tree-using-dfs/

from typing import List


class Solution:
    def __init__(self, count: int) -> None:
        self.node_count = count
        self.start: list[int] = [0] * self.node_count
        self.end: list[int] = [0] * self.node_count
        self.dfs_nodes: list[int] = []
        self.adj: list[list[int]] = [[] for _ in range(self.node_count)]
        # assume 1 node has 1 parent, visited is not necessary
        # self.visited: list[bool] = [False] * self.node_count

    def add_node(self, node_index: int, node_child: int):
        self.adj[node_index].append(node_child)

    def dfs(self, index: int, dfs_nodes_index: int) -> int:
        # +1 cause start from first child of this node to include in subtree
        dfs_nodes_index += 1
        self.start[index] = dfs_nodes_index
        self.dfs_nodes.append(index)
        for child in self.adj[index]:
            dfs_nodes_index = self.dfs(child, dfs_nodes_index)
        # dfs_nodes_index will be last node (bottomest rightmost)
        # from this node. When this function in last traversed node, it will
        # return +1  to index cause it is added by default
        self.end[index] = dfs_nodes_index
        return dfs_nodes_index

    def print_subtrees(self):
        for i in range(self.node_count):
            if self.start[i] != self.end[i]:
                print("subtree of node", i, "is", end=" ")
                for j in range(self.start[i], self.end[i]):
                    print(self.dfs_nodes[j], end=" ")
                print()


class GeeksforGeeks:
    def __init__(self) -> None:
        # Python3 code to print subtree of all nodes

        # arrays for keeping position at
        # each dfs traversal for each node
        self.start: List[int] = [0] * 100001
        self.end: List[int] = [0] * 100001

        # Storing dfs order
        self.dfs_order: List[int] = []
        self.adj: List[List[int]] = [[] for _ in range(100001)]
        self.visited = [False] * 100001

    # Recursive function for dfs traversal dfsUtil()
    def dfs(self, a: int, b: int) -> int:
        """
        a: starting node, usually root
        b:
        """
        # keep track of node visited
        self.visited[a] = True
        b += 1
        self.start[a] = b
        self.dfs_order.append(a)

        for it in self.adj[a]:
            if not self.visited[it]:
                b = self.dfs(it, b)

        self.end[a] = b
        return b

    # Function to print the subtree nodes

    def Print(self, n: int):
        for i in range(0, n):
            # If node is leaf node
            # start[i] is equals to endd[i]
            if self.start[i] != self.end[i]:
                print("subtree of node", i, "is", end=" ")
                for j in range(self.start[i] + 1, self.end[i] + 1):
                    print(self.dfs_order[j - 1], end=" ")

                print()


def main_g4g():
    # This code is contributed by Rituraj Jain
    # Driver code
    # No of nodes n = 10
    n, c = 10, 0
    gfg = GeeksforGeeks()
    gfg.adj[0].append(1)
    gfg.adj[0].append(2)
    gfg.adj[0].append(3)
    gfg.adj[1].append(4)
    gfg.adj[1].append(5)
    gfg.adj[4].append(7)
    gfg.adj[4].append(8)
    gfg.adj[2].append(6)
    gfg.adj[6].append(9)

    # Calling dfs for node 0
    # Considering root node at 0
    gfg.dfs(0, c)

    # Print child nodes
    gfg.Print(n)


def main():
    sol = Solution(10)
    sol.add_node(0, 1)
    sol.add_node(0, 2)
    sol.add_node(0, 3)
    sol.add_node(1, 4)
    sol.add_node(1, 5)
    sol.add_node(4, 7)
    sol.add_node(4, 8)
    sol.add_node(2, 6)
    sol.add_node(6, 9)
    sol.dfs(0, 0)
    # print(sol.dfs_nodes)
    # print(sol.start)
    # print(sol.end)
    sol.print_subtrees()


if __name__ == "__main__":
    main()
    main_g4g()
