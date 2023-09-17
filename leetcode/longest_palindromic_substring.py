class Solution:
    # abbbabbbd
    # 1111112345654321
    count = 0

    def longestPalindrome1(self, s: str) -> str:
        def _checkPalindrome1(s: str) -> str:
            Solution.count += 1
            if len(s) == 1:
                return s
            m = len(s) // 2  # if odd return 1 else 0
            if len(s) % 2:
                # odd
                if s[:m] == s[m + 1 :][::-1]:
                    return s
                else:
                    a = _checkPalindrome1(s[: len(s) - 1])
                    b = _checkPalindrome1(s[1:])
                    if len(a) > len(b):
                        return a
                    else:
                        return b
            else:
                # even
                # print(s[:m])
                # print(s[m:][::-1])
                if s[:m] == s[m:][::-1]:
                    return s
                else:
                    a = _checkPalindrome1(s[: len(s) - 1])
                    b = _checkPalindrome1(s[1:])
                    if len(a) > len(b):
                        return a
                    else:
                        return b

        return _checkPalindrome1(s)

    def longestPalindrome2(self, s: str) -> str:
        if len(s) == 1:
            return s
        for i in range(len(s) - 1):
            pass


if __name__ == "__main__":
    ss = ["a", "aa", "aba", "aaba", "abaa", "aaaaabbbddbbb"]
    for s in ss:
        sol = Solution()
        ans = sol.longestPalindrome1(s)
        print(ans)
        print(f"count={sol.count}")
