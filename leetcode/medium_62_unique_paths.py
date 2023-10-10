class Solution:
    @staticmethod
    def solve(m: int, n: int):
        row = [1] * n

        for _ in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]
            row = new_row

        return row[0]


def main():
    ans = Solution.solve(7, 3)
    print(f"ans={ans} correct ans=28")


if __name__ == "__main__":
    main()
