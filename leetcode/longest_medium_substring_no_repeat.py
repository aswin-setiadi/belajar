from typing import Set


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, s: str) -> int:
        print(f"solving {s}")
        # if use set, later can't retrieve the longest substring
        ss = ""
        ans = ss
        maxlen = 0
        for i in range(len(s)):
            if s[i] not in ss:
                ss += s[i]
                if len(ss) > maxlen:
                    ans = ss
                    maxlen = len(ss)

            else:
                for j in range(len(ss)):
                    if ss[j] == s[i]:
                        index = j + 1
                        if index == len(ss):
                            ss = s[i]
                        else:
                            ss = ss[index:] + s[i]
                        break

        print(ans)
        print(maxlen)
        return maxlen

    def neetcode_sol(self, s: str) -> int:
        charSet: Set[str] = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, r - l + 1)  # +1 for l itself
        print(res)
        return res


if __name__ == "__main__":
    sample = "abcabcbbabcdefgg"  # 7 abcdefg
    tes = "adefdbc"  # 5 efdabc
    tes2 = "abccd"  # 3 abc
    tes3 = "abccdef"  # 4 cdef
    tes4 = "abcadf"  # 5 bcadf
    tes5 = "abcbd"  # 3 abc
    # Solution().solve(sample)
    # Solution().solve(tes)
    # Solution().solve(tes2)
    # Solution().solve(tes3)
    # Solution().solve(tes4)
    # Solution().solve(tes5)
    # print("neetcode way")
    # Solution().neetcode_sol(sample)
    # Solution().neetcode_sol(tes)
    # Solution().neetcode_sol(tes2)
    # Solution().neetcode_sol(tes3)
    # Solution().neetcode_sol(tes4)
    Solution().neetcode_sol(tes5)
