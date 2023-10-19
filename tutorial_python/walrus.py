def main():
    i: int = 0
    # walrus operator can't have 2 in same line somehow, it will say 2nd var undefined
    while is_true := i < 5:
        print(f"{i} {is_true}")
        i += 1


if __name__ == "__main__":
    main()
