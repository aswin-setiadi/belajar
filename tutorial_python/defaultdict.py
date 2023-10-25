# Python program to demonstrate
# defaultdict


from collections import defaultdict


def main():
    # Function to return a default
    # values for keys that is not
    # present
    def def_value():
        return "Not Present"

    # Defining the dict
    d = defaultdict(def_value)
    d["a"] = 1
    d["b"] = 2
    print(d)
    print(d["a"])
    print(d["b"])
    print(d["c"])
    print(def_value)


def main2():
    d = defaultdict(dict)
    d["b"]["b"] = 1
    print(d)


if __name__ == "__main__":
    main()
    main2()
