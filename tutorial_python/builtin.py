from collections import deque
from functools import reduce
from typing import Any


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


q: deque[Any] = deque([1, 2, 3, 4], 3)
q.append("a")
q.append("b")
q.append("c")
q.append("d")
print(q)
q.appendleft("a")
print(q)
q.pop()
q.popleft()
print(len(q))
if q:
    print("q not empty")

# for stack can use list append and pop, deque is faster than list cause:
# when python need to reallocate memory to grow underlying list, the operation are slower and can become O(n)


def main_set():
    # python set is unordered and after created, element cant be changed but can add/ remove and must unique
    # set element must be immutable type
    s0 = {2}
    s1 = {1, 2, 3, 3}  # will be 1,2,3
    s2 = {1, 4}

    # | operator need both as set, union() method can take any iterable as arg,
    # same for intersection, difference
    s3 = s1 | s2  # 1,2,3,4 same for s1.union(s2)
    s4 = s1.union(s2, s3)  # same for s1 | s2 | s3
    s5 = s1.intersection(s2)  # 1, s1 & s2 for same result
    diff = s1.difference(s2)  # or s1-s2 result is {2,3}
    # unlike ^ and other methods, the method does not allows multiple set args
    s_d = s1.symmetric_difference(s2)  # or s1 ^ s2, return 2,3,4

    # true if no common item, else false, no operator equivalent
    no_common = s1.isdisjoint(s2)
    is_subset = s0.issubset(s1)  # true, alternative= s0 <= s1
    is_proper_subset = s0 < s1  # true since both not identical, no alternative method
    is_superset = s1.issuperset(s0)  # true, alternative s1 >= s0
    # true cause have extra element in s1 that is not in s0
    is_proper_superset = s1 > s0
    # augmented assignment are the 4 operation below:
    x1 = set((1, 2, 3))
    x2 = {1, 3, 4}
    x1 |= x2  # 1,2,3,4 same as x1.update(x2) where x2 is an iterable obj
    x1 = {1, 2, 3}
    x2 = {1, 3, 4}
    x1.intersection_update(x2)  # x1 will be 1,3 same as x1 &= x2
    x1 = {1, 2, 3}
    x2 = {1, 3, 4}
    x1.difference_update(x2)  # same as x1 -= x2, x1 will be 2
    x1 = {1, 2, 3}
    x2 = {1, 3, 4}
    x1.symmetric_difference_update(x2)  # x1 will be 2,4 same as x1 ^= x2

    x1.add(1)  # 1,2,4 arg must be single immutable obj
    x1.add(1)  # does nothing since it exist
    x1.remove(3)  # raise error
    x1.discard(3)  # does nothing cause it does not exist
    x1.pop()  # delete and return random element, raise error if empty
    s1.clear()  # remove all elements

    # frozenset same as set except it is immutable
    # but augmented assignment does not operate in place but create new set
    # so it works
    f = frozenset((1, 2, 3, 1))  # 1,2,3
    # f = f & {1}  # it works and f will be frozenset({1})
    f.intersection({1})  # return new frozenset
    # frozenset is useful if you need set as immutable obj
    # maybe you want  set of set? since element of set must be immutable
    # so you will have set of frozenset


# tuple is non-unique ordered and element is unchangeable and can't add/ remove
# (4) is int, (4,) is tuple
# dict is ordered (as of 3.7) and changeable
# deque append and popleft= queue
# deque append and pop= stack
