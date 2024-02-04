def is_even(x: int) -> bool:
    if x % 2 == 0:
        return True
    else:
        return False


def main():
    i: int = 0
    # walrus operator can't have 2 in same line somehow, it will say 2nd var undefined
    while is_true := i < 5:
        # if is_true walrus above in bracket, is_true will be number instead of bool
        print(f"{i} {is_true}")
        i += 1
    # https://www.youtube.com/watch?v=nrN3Gq1A92Y
    l = [1, 2, 3, 4]
    l_b = [(_, y) for _ in l if (y := is_even(_))]
    print(l_b)


if __name__ == "__main__":
    main()
