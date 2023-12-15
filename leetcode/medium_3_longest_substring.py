#!/bin/python3
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    # 5.78% 63.8%
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest: int = 1
        dic: dict[str, int] = {}
        start: int = 0
        end: int = 0
        for index in range(len(s)):
            cur_char = s[index]
            if dic.get(cur_char) is not None:
                # exist
                longest = max(longest, (end - start + 1))
                # update dict, remove memory of char before the first occurance of the duplicate+1
                tmp = {cur_char: index}
                start = index
                for k, v in dic.items():
                    if k != cur_char and v > dic[cur_char]:
                        tmp[k] = v
                        start = min(start, v)
                dic = tmp

            else:
                dic[s[index]] = index
                end = index
        # need to take account the last
        longest = max(longest, (end - start + 1))
        return longest


if __name__ == "__main__":
    ss = ["abcabcabc", "bbbbb", "abcabcbb", "  ", "", "tmmzuxt", "dvdf"]
    anss = [3, 1, 3, 1, 0, 5, 3]
    for s in ss[:]:
        ans = Solution().lengthOfLongestSubstring(s)
        print(ans)
