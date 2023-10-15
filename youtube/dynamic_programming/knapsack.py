class Solution:
    """
    https://www.youtube.com/watch?v=xOlhR_2QCXY&t=304s
    """

    def __init__(self, ws: list[int], vs: list[int]) -> None:
        self.ws = ws
        self.vs = vs
        self.memory: dict[int, dict[int, int]] = {}

    def solve_naive(self, n: int, C: int) -> int:
        if n == len(self.ws) or C == 0:
            result = 0
        elif self.ws[n] > C:
            result = self.solve_naive(n + 1, C)
        else:
            tmp1 = self.solve_naive(n + 1, C)
            tmp2 = self.vs[n] + self.solve_naive(n + 1, C - self.ws[n])
            result = max(tmp1, tmp2)
        return result

    def solve(self, n: int, C: int) -> int:
        if n in self.memory:
            if C in self.memory[n]:
                return self.memory[n][C]
        if n == len(self.ws) or C == 0:
            result = 0
        elif self.ws[n] > C:
            result = self.solve_naive(n + 1, C)
        else:
            tmp1 = self.solve(n + 1, C)
            tmp2 = self.vs[n] + self.solve(n + 1, C - self.ws[n])
            result = max(tmp1, tmp2)
            if n not in self.memory:
                self.memory[n] = {}
            self.memory[n][C] = result
        return result


def main():
    w = [1, 2, 4, 2, 5]
    v = [5, 3, 5, 3, 2]
    C = 10
    ans = Solution(w, v).solve(0, C)
    print(ans)


if __name__ == "__main__":
    main()
