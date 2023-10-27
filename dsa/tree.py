class Tree:
    """
    parent node= node before current node
    child node= nodes after current node
    root= top
    #leaf/ external= nodes that don't have child
    ancestors= all dad, granddad, etc. of the node
    descendant= all nodes from the leaf of the path to the node
    sibling= node with same parent
    level of a node= count of edges from the node to root
    internal node= node with at least 1 child
    neighbour= parent or child
    subtree= any node of the tree with its descendant

    Tree properties
    one and only one path between every vertices
    edges= nodes-1
    depth of node= # of edge from root to that node
    height of tree= leaf with most edges from root, root is 0
    degree of node= total no. of children of that node
    degree of tree= highest degree of a node in that tree
    order of tree= number of children the tree can have
    """

    def __init__(self, node_count: int, adj: list[list[int]]) -> None:
        self.N = node_count
        self.root = 0
        self.adj = adj

    def printParents(self, node: int, parent: int) -> None:
        if node == self.root:
            print("0->root")
        else:
            print(f"{node}->{parent}")
        for cur in self.adj[node]:
            if cur != parent:
                self.printParents(cur, node)

    def printChildren(self, node: int, parent: int) -> None:
        children = [n for n in self.adj[node] if n != parent]
        print(f"{node}->{children}")
        for cur in self.adj[node]:
            if cur != parent:
                self.printChildren(cur, node)

    def printLeafNodes(self, node: int, parent: int) -> None:
        # leaf node will have 1 adj which is parent only
        if len(self.adj[node]) == 1:
            print(f"{node} is leaf")
        for cur in self.adj[node]:
            if cur != parent:
                self.printLeafNodes(cur, node)

    def printDegrees(self):
        print(f"0 (root) degree={len(self.adj[0])}")
        for i, v in enumerate(self.adj[1:], start=1):
            print(f"{i} degree={len(v)-1}")


def main():
    n = 7
    adj: list[list[int]] = [[] for _ in range(n)]
    adj[0].append(1)
    adj[1].append(0)
    adj[0].append(2)
    adj[2].append(0)
    adj[0].append(3)
    adj[3].append(0)
    adj[1].append(4)
    adj[4].append(1)
    adj[1].append(5)
    adj[5].append(1)
    adj[3].append(6)
    adj[6].append(3)
    tree = Tree(n, adj)
    tree.printParents(0, 0)
    tree.printChildren(0, 0)
    tree.printLeafNodes(0, 0)
    tree.printDegrees()


if __name__ == "__main__":
    main()
