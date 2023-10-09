from functools import reduce

fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]


def starts_with_A(s):
    if s[0] == "A":
        return s  # or True, so will be True, None, etc.
    # auto else to None, so must declare


map_object = map(starts_with_A, fruits)
print(list(map_object))

filter_object = filter(lambda x: x[0] == "A", fruits)
print(list(filter_object))

print(reduce(lambda x, y: x + y, fruits))
