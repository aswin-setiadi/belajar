class TreeNode:
    def __init__(
        self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def solve(arr: list[int]) -> None | TreeNode:
        def _helper(l: int, r: int) -> None | TreeNode:
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(arr[m])
            root.left = _helper(l, m - 1)
            root.right = _helper(m + 1, r)
            return root

        return _helper(0, len(arr) - 1)


def main():
    """
        0
    -10      5
        -3      9
    """
    arr = [-10, -3, 0, 5, 9]
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = Solution.solve(arr)
    print("end")


if __name__ == "__main__":
    main()
