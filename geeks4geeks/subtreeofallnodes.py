#!/bin/python3
# https://www.geeksforgeeks.org/sub-tree-nodes-tree-using-dfs/

from typing import List

# Python3 code to print subtree of all nodes

# arrays for keeping position at
# each dfs traversal for each node
start: List[int] = [0] * 100001
end: List[int] = [0] * 100001

# Storing dfs order
dfs_order: List[int] = []
adj: List[List[int]] = [[] for _ in range(100001)]
visited = [False] * 100001

# Recursive function for dfs traversal dfsUtil()


def dfs(a: int, b: int) -> int:
    """
    a: starting node, usually root
    b:
    """
    # keep track of node visited
    visited[a] = True
    b += 1
    start[a] = b
    dfs_order.append(a)

    for it in adj[a]:
        if not visited[it]:
            b = dfs(it, b)

    end[a] = b
    return b


# Function to print the subtree nodes


def Print(n: int):
    for i in range(0, n):
        # If node is leaf node
        # start[i] is equals to endd[i]
        if start[i] != end[i]:
            print("subtree of node", i, "is", end=" ")
            for j in range(start[i] + 1, end[i] + 1):
                print(dfs_order[j - 1], end=" ")

            print()


# Driver code
if __name__ == "__main__":
    # No of nodes n = 10
    n, c = 10, 0

    adj[0].append(1)
    adj[0].append(2)
    adj[0].append(3)
    adj[1].append(4)
    adj[1].append(5)
    adj[4].append(7)
    adj[4].append(8)
    adj[2].append(6)
    adj[6].append(9)

    # Calling dfs for node 0
    # Considering root node at 0
    dfs(0, c)

    # Print child nodes
    Print(n)

# This code is contributed by Rituraj Jain
