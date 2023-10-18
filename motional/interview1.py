class Solution:
    @staticmethod
    def solve_fixed_limit(velocities: list[tuple[int, int]]) -> list[tuple[int, int]]:
        start = None
        speed_limit = 10
        ans: list[tuple[int, int]] = []
        for item in velocities:
            if item[1] > speed_limit:
                if start is None:
                    start = item[0]
            else:
                # below speed limit
                if start is not None:
                    ans.append((start, item[0]))
                    start = None
        if start is not None:
            ans.append((start, velocities[-1][0] + 1))
        return ans

    @staticmethod
    def solve(
        velocities: list[tuple[int, int]], limits: list[tuple[int, int]]
    ) -> list[tuple[int, int]]:
        start = None
        speed_limit = limits[0][0]
        limits_index = 1
        ans: list[tuple[int, int]] = []
        for item in velocities:
            if limits_index < len(limits):
                if limits[limits_index][0] <= item[0]:
                    speed_limit = limits[limits_index][1]
                    limits_index += 1

            if item[1] > speed_limit:
                if start is None:
                    start = item[0]
            else:
                # below speed limit
                if start is not None:
                    ans.append((start, item[0]))
                    start = None

        if start is not None:
            ans.append((start, velocities[-1][0] + 1))

        return ans


def main():
    v: list[tuple[int, int]] = [
        (0, 9),
        (1, 11),
        (3, 10),
        (4, 11),
        (5, 12),
        (7, 13),
        (8, 10),
        (9, 11),
    ]
    limits: list[tuple[int, int]] = [(0, 5), (4, 12)]
    ans = Solution.solve_fixed_limit(v)
    print(ans)
    ans = Solution.solve(v, limits)
    print(ans)


if __name__ == "__main__":
    main()
