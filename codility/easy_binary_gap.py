def solution(N: int):
    # Implement your solution here
    if N < 2:
        return 0
    b = bin(N)[2:]
    print(b)
    cumulator = 0
    longest = 0
    for d in b:
        if d == "1":
            longest = max(longest, cumulator)
            cumulator = 0
        else:
            cumulator += 1
    return longest


def main():
    print(solution(1041))


if __name__ == "__main__":
    main()
