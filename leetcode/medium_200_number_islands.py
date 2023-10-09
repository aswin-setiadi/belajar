class Solution:
    # 46.41% 83.84%
    def _get_neigbour_land(self, r: int, c: int) -> list[tuple[int, int]]:
        ns: list[tuple[int, int]] = []
        if r >= 1:
            new_r1 = r - 1
            ns.append((new_r1, c))
        if r < self.max_r - 1:
            new_r2 = r + 1
            ns.append((new_r2, c))
        if c >= 1:
            new_c1 = c - 1
            ns.append((r, new_c1))
        if c < self.max_c - 1:
            new_c2 = c + 1
            ns.append((r, new_c2))
        return ns

    def _explore_lands(self, r: int, c: int):
        if self.visited[r][c] is False:
            self.visited[r][c] = True
            if self.matrix[r][c] == "1":
                ns = self._get_neigbour_land(r, c)
                for n in ns:
                    self._explore_lands(n[0], n[1])

    def numIslands(self, grid: list[list[str]]) -> int:
        self.matrix = grid
        self.max_r = len(self.matrix)
        self.max_c = len(self.matrix[0])
        self.visited: list[list[bool]] = [
            [False] * self.max_c for _ in range(self.max_r)
        ]
        self.total_land = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.visited[i][j] == False:
                    self.visited[i][j] = True
                    if self.matrix[i][j] == "1":
                        self.total_land += 1
                        ns = self._get_neigbour_land(i, j)
                        for n in ns:
                            self._explore_lands(n[0], n[1])

        return self.total_land


if __name__ == "__main__":
    grids = [
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
    ]
    for g in grids:
        ans = Solution().numIslands(g)
        print(ans)
