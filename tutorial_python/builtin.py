from collections import deque
from functools import reduce


def main():
    def starts_with_A(s: str):
        if s[0] == "A":
            return s  # or True, so will be True, None, etc.
        # auto else to None, so must declare

    fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
    map_object = map(starts_with_A, fruits)
    print(list(map_object))

    filter_object = filter(lambda x: x[0] == "A", fruits)
    print(list(filter_object))

    print(reduce(lambda x, y: x + y, fruits))


q: deque[str] = deque()
q.append("a")
q.append("b")
q.append("c")
q.pop()
q.popleft()
print(q.appendleft("a"))

# for stack can use list append and pop, deque is faster than list cause:
# when python need to reallocate memory to grow underlying list, the operation are slower and can become O(n)

# python set is unordered and after created, element cant be changed but can add/ remove and must unique
# tuple is ordered and element is unchangeable and can't add/ remove
# deque append and popleft= queue
# deque append and pop= stack
