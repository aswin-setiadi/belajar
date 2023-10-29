def outer(l: list[int]):
    print("out")

    def inner():
        print("in")
        print(l[0])

    return inner


v = outer([1])
v()  # will keep l ref hence when called still can print 1
