from queue import Queue


class Edge:
    def __init__(self, multiplier: float, pointer: "Node") -> None:
        self.multiplier = multiplier
        self.target = pointer


class Node:
    def __init__(self, unit: str) -> None:
        self.unit = unit
        self.edges: list[Edge] = []

    def add_edge(self, multiplier: float, target: "Node"):
        self.edges.append(Edge(multiplier, target))


def parse_facts(facts: list[tuple[str, float | int, str]]):
    name_to_node: dict[str, Node] = {}
    for left, multiplier, right in facts:
        if left not in name_to_node:
            left_node = Node(left)
            name_to_node[left] = left_node
        if right not in name_to_node:
            right_node = Node(right)
            name_to_node[right] = right_node
        name_to_node[left].add_edge(multiplier, name_to_node[right])
        name_to_node[right].add_edge(1 / multiplier, name_to_node[left])
    return name_to_node


def solve(
    amt: float | int,
    start_unit: str,
    end_unit: str,
    facts: list[tuple[str, float | int, str]],
):
    name_to_node = parse_facts(facts)
    if start_unit not in name_to_node or end_unit not in name_to_node:
        return -1
    else:
        visited: list[Node] = []
        search_queue: Queue[tuple[float, Node]] = Queue()
        search_queue.put((amt, name_to_node[start_unit]))
        final_amt = -1
        while not search_queue.empty():
            current_amt, current_node = search_queue.get()
            for edge in current_node.edges:
                if edge.target not in visited:
                    visited.append(edge.target)
                    if edge.target == name_to_node[end_unit]:
                        final_amt = current_amt * edge.multiplier
                        break
                    else:
                        search_queue.put((current_amt * edge.multiplier, edge.target))
        return final_amt


def testt(l: list[tuple[int]]):
    print(l)


if __name__ == "__main__":
    # facts = [("m", 10, "dm"), ("dm", 10, "cm"), ("cm", 10, "mm"), ("m", 1000, "mm")]
    # facts = [("m", 10, "dm"), ("dm", 10, "cm"), ("cm", 10, "mm")]
    facts = [("kg", 1000, "g"), ("m", 10, "dm"), ("dm", 10, "cm"), ("cm", 10, "mm")]
    # facts = [("m", 1000, "mm")]
    ans = solve(1, "m", "mm", facts)
    print(ans)
    l = [(1,), (2,)]
    testt(l)
