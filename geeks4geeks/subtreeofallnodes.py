#!/bin/python3
# https://www.geeksforgeeks.org/sub-tree-nodes-tree-using-dfs/

from typing import List


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


# Driver code
if __name__ == "__main__":
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

# This code is contributed by Rituraj Jain
