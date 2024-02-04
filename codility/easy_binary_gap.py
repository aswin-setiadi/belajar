def to_bin(n: int) -> str:
    ans: list[str] = []
    while n != 0:
        tmp = n % 2
        ans.append(str(tmp))
        n = n // 2
    ans.extend(["b", "0"])
    ans.reverse()

    return "".join(ans)


def solution(N: int):
    # Implement your solution here
    if N < 2:
        return 0
    b = to_bin(N)[2:]
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
