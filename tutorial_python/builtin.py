from collections import deque
from functools import reduce
import string
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


def main_queue():
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


def main_tuple():
    # tuple is non-unique ordered and element is unchangeable and can't add/ remove
    # (4) is int, (4,) and 4, is tuple
    # tuple is lightweight, indexable, immutable, heterogeneous (can store multiple obj type),
    # iterable, sliceable, combinable (concat), hashable
    # unpacking var must match iterable (tuple in this case) length
    # since 3.5 unpacking works for iterable objs not just tuple
    # tuple has index and count method to check index and count of an obj in it
    # when using "in" e.g. "Monday" in days, it is O(n)
    # so better use set since it is implemented as hash table
    # builtin reversed and sorted will return new obj

    first, last = ["Aswin", "Setiadi"]

    name, age, height, country = ("Jane Doe", 25, 1.75, "Canada")
    days = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )
    empty = ()
    no_brackets = 1, 2, 3
    t = tuple([True, 1, ["a", "b"]])
    t[2].append("c")
    first, *middles, last = (1, 2, 3, 4, 5)  # middles will be list
    name = ("Aswin", "Setiadi")
    contact = ("aswin.setiadi@gmail.com", 12345678)
    aswin = (*name, *contact)
    quotient, remainder = divmod(7, 2)
    t1 = (1,)
    t2 = t1[:]  # same as copy(t1) copy is from copy import copy
    is_same = id(t1) == id(t2)  # True

    info1 = ("Aswin", 31)
    info2 = ("Computer Science", ("Python", "Flask"))
    info3 = ("12345678",)
    info4 = info1 + info2 + info3  # can only concat. tuple with tuple
    num = (1, 2, 3)
    num_twice = num * 2  # 1,2,3,1,2,3

    fruits = (("apple", 0.4), ("banana", 0.25), ("orange", 0.35))
    sorted_by_price_fruits = sorted(fruits, key=lambda fruit: fruit[1])

    monthly_incomes = (
        ("January", 5000),
        ("February", 5500),
        ("March", 6000),
        ("April", 5800),
        ("May", 6200),
        ("June", 7000),
        ("July", 7500),
        ("August", 7300),
        ("September", 6800),
        ("October", 6500),
        ("November", 6000),
        ("December", 5500),
    )
    quarter_income = 0
    for i, (month, income) in enumerate(monthly_incomes, start=1):
        print(f"{month:>10}: {income}")
        quarter_income += income
        if i % 3 == 0:
            print("-" * 20)
            print(f"{'Quarter':>10}: {quarter_income}", end="\n\n")
            quarter_income = 0

    numbers = "2", "3", "1"
    tuple_int = tuple(int(number) for number in numbers)
    print(tuple_int)


def main_list():
    # list method reverse and sort apply in place
    # list elements are more for homogenous use
    l = [1, 2, 3]
    l.insert(1, 1.5)  # 1,1.5,2,3
    ll = sorted(l, reverse=True)  # sort in descending


def lambda_tutorial():
    result = (lambda x, y: x + y)(10, 20)
    print(result)
    l = [1, 2, 3, 4, 5]
    nl = list(map(lambda x, y: x + y, l, l))
    print(nl)


def thousand_seperator():
    x = string.ascii_uppercase * int(1e3)  # repeat A-Z 1e3 times
    thousand = 1000
    print(f"{thousand:,}")


# dict is ordered (as of 3.7) and changeable
# deque append and popleft= queue
# deque append and pop= stack

if __name__ == "__main__":
    # lambda_tutorial()
    main_tuple()
