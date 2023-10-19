class Solution:
    """36.73% 17.68%"""

    def addStrings(self, num1: str, num2: str) -> str:
        ans: list[str] = []
        carry: int = 0
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0 or carry != 0:
            if i >= 0:
                n1 = int(num1[i])
                carry += n1
                i -= 1
            if j >= 0:
                n2 = int(num2[j])
                carry += n2
                j -= 1
            ans.append(str(carry % 10))
            carry //= 10

        return "".join(reversed(ans))


def main():
    ans = Solution().addStrings("992", "99")
    print(ans)


if __name__ == "__main__":
    main()
