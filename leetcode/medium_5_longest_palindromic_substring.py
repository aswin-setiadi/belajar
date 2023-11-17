class Solution:
    # abbbabbbd
    # 1111112345654321
    count = 0

    # time complexity 2^n
    def longestPalindrome1(self, s: str) -> str:
        def _checkPalindrome1(s: str) -> str:
            Solution.count += 1
            if len(s) == 1:
                return s
            m = len(s) // 2  # floor division
            # if odd return 1 else 0
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

    # neetcode answer
    def longestPalindrome2(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        Solution.count = resLen
        return res


if __name__ == "__main__":
    ss = ["a", "aa", "aba", "aaba", "abaa", "aaaaabbbddbbb"]
    for s in ss:
        sol = Solution()
        ans = sol.longestPalindrome2(s)
        print(ans)
        print(f"count={sol.count}")
