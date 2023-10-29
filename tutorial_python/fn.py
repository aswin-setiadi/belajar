import timeit


def outer(l: list[int]):
    print("out")

    def inner():
        print("in")
        print(l[0])

    return inner


v = outer([1])
print(v)  # inner function
v()  # will keep l ref hence when called still can print 1
# number= count of timer call, repeat= count of timeit call
ans = min(timeit.repeat(outer([1, 2]), repeat=2, number=3))
print(ans)
