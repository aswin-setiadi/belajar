class Solution:
    @classmethod
    def array_product(cls, l: list[int]) -> list[int]:
        n = len(l)
        final_arr = [1] * n
        prefix = 1
        postfix = 1
        for i in range(n):
            final_arr[i] = prefix
            prefix = prefix * l[i]
        for i in range(n - 1, -1, -1):
            final_arr[i] *= postfix
            postfix *= l[i]
        return final_arr


if __name__ == "__main__":
    l = [1, 2, 3, 4, 0, 5, 6, -7, 0]
    print(Solution.array_product(l))
