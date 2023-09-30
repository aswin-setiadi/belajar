# if start ==n and end ==n print result


class Solution:
    @classmethod
    def solve_recursive(cls, n: int):  # in g4g, this is their dfs result
        def _attempt(s, pos, start, stop):
            if stop == n:
                print(s)
                return
            if start < n:
                # s = s + "{"
                # at start= n, attempt will be called here and below, which will produce duplicate
                # _attempt(s, pos + 1, start+1, stop)
                _attempt(s + "{", pos + 1, start + 1, stop)
            if stop < start:
                s = s + "}"
                _attempt(s, pos + 1, start, stop + 1)
            # print("exit")

        if n < 1:
            return -1
        _attempt("", 0, 0, 0)

    @classmethod
    def solve_recursive2(cls, n: int):  # geeksforgeeks answer
        def _attempt(s, pos, start, stop):
            if stop == n:
                # for c in s:
                #     print(c, end="")
                # print()
                print(("").join(s))
                return
            if start > stop:
                s[pos] = "}"
                _attempt(s, pos + 1, start, stop + 1)
            if start < n:
                s[pos] = "{"
                _attempt(s, pos + 1, start + 1, stop)
            print("exit")

        tmp = [""] * 2 * n
        if n < 1:
            return -1
        _attempt(tmp, 0, 0, 0)


if __name__ == "__main__":
    Solution().solve_recursive(3)
