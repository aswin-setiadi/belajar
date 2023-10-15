class Solution:
    # leetcode solution, I wasn't familiar with pow properties
    @staticmethod
    def myPow(x: float, n: int) -> float:
        """
        2**6= (2**2)**3, hence divide by 2 for each base multiplication
        = keep 1 (2**2) multiply to ans variable, so we can 3-1
        2^2 x 2^3= 2^(2+3)
        0^0-n= 1
        0^-n not possible
        68.12% 55.84%
        removing n==0 check (-1^0 is still 1), speed+memory become 40.17% 85.53%
        """

        if x == 0:
            return 0

        power = abs(n)
        ans = 1
        base = x
        while power != 0:
            # odd
            if power % 2 == 1:
                ans *= base
                power -= 1
            # even
            else:
                base *= base
                power = power // 2
        return ans if n >= 0 else 1 / ans


def main():
    for t in [
        (-2, -2),
        (-2, 0),
        (-2, 2),
        (-2, 3),
        (0, 0),
        (0, 2),
        (2, -2),
        (2, 0),
        (2, 16),  # 2 16, 4 8, 16 4, 32 2, 65536 1, ans=1x65536
        (
            2,
            15,
        ),  # ans=1x2, 2 14, 4 7, ans=2x4, 16 3, ans= 8x16, 16 2, 256 1, ans= 128*256=32768
        (-2, 16),
        (-2, 15),
    ]:
        ans = Solution.myPow(t[0], t[1])
        print(f"t={t} ans={ans}")


if __name__ == "__main__":
    main()
