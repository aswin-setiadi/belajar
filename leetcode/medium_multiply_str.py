from itertools import zip_longest


class Solution:
    """
    len(num1xnum2) <= len(num1)+len(num2)
    """

    def multiply(self, num1: str, num2: str) -> str:
        # loop num2 from least sig digit
        # loop again num1 from least sig digit and multiply by num2 least significant digit
        # add previous carry to multiply result, update the new carry for next digit
        # when num1 loop finish, if have carry, add result with carry*10^len(result)
        # store in tmp_result
        # when loop num2 finish, sum both result and return as str

        # example= 123+456=
        # 837
        # 0516
        # 00294
        # during sum, suffix 0

        # 27.66% 31.6%
        if num1 == "0" or num2 == "0":
            return "0"

        result: list[list[int]] = []
        for i, d2 in enumerate(num2[::-1]):
            d2_int = int(d2)
            carry = 0
            tmp_result: list[int] = [0] * i
            for d1 in num1[::-1]:
                d1_int = int(d1)
                multiply = d1_int * d2_int + carry
                digit = multiply % 10
                carry = multiply // 10
                tmp_result.append(digit)
            if carry != 0:
                tmp_result.append(
                    carry
                )  # reversed order, with zero prefix for different num2 digit
            result.append(tmp_result)

        # sum
        if len(result) == 1:
            ans = [str(v) for v in result[0][::-1]]
            return "".join(ans)
        else:
            mid_ans = result[0]  # will be reversed
            for r in result[1:]:
                tmp_ans: list[int] = []
                mid_ans.extend([0] * (len(r) - len(mid_ans)))
                sum_carry = 0
                for i in range(len(mid_ans)):
                    digit_sum = mid_ans[i] + r[i] + sum_carry
                    digit = digit_sum % 10
                    sum_carry = digit_sum // 10
                    tmp_ans.append(digit)
                if sum_carry:
                    tmp_ans.append(sum_carry)
                mid_ans = tmp_ans
            return "".join([str(d) for d in mid_ans[::-1]])

    def multiply_inplace(self, num1: str, num2: str) -> str:
        # 25.49%, 7.68%
        if num1 == "0" or num2 == "0":
            return "0"
        ans = [0] * (len(num1) + len(num2))
        for (
            i,
            d2,
        ) in enumerate(num2[::-1]):
            d2_int = int(d2)
            mid_ans: list[int] = [0] * i
            carry = 0
            for d1 in num1[::-1]:
                d1_int = int(d1)
                d2_m_d1 = d2_int * d1_int + carry
                digit = d2_m_d1 % 10
                carry = d2_m_d1 // 10
                mid_ans.append(digit)
            if carry:
                mid_ans.append(carry)

            # add ans with mid_ans
            Solution._sum_inplace(mid_ans, ans)

        ans_l = [str(v) for v in ans]
        while ans_l[-1] == "0":
            ans_l.pop(-1)
        return "".join(reversed(ans_l))

    def multiply_inplace2(self, num1: str, num2: str) -> str:
        # 37.64% 63.19%
        if num1 == "0" or num2 == "0":
            return "0"
        ans: list[int] = [0] * (len(num1) + len(num2))
        for i, d2 in enumerate(num2[::-1]):
            d2_int = int(d2)
            for j, d1 in enumerate(num1[::-1]):
                d1_int = int(d1)
                ans_start = i + j
                carry = ans[ans_start]
                d2_m_d1 = d2_int * d1_int + carry
                ans[ans_start] = d2_m_d1 % 10
                ans[ans_start + 1] += d2_m_d1 // 10

        while ans[-1] == 0:
            ans.pop()

        return "".join([str(v) for v in ans[::-1]])

    @classmethod
    def _sum_inplace(cls, mid_ans: list[int], ans: list[int]):
        carry_sum = 0
        for i, v in enumerate(mid_ans):
            tmp_sum = ans[i] + v + carry_sum
            digit = tmp_sum % 10
            carry_sum = tmp_sum // 10
            ans[i] = digit
        if carry_sum:
            ans[len(mid_ans)] += carry_sum


def zip_long_example():
    l = [1, 2, 3]
    l2 = [1, 2, 3, 4]
    lt1 = list(
        zip(
            l,
            l2,
        )
    )

    lt2 = list(zip_longest(l, l2, fillvalue=None))
    print(lt1)
    print(lt2)


if __name__ == "__main__":
    qns = [("123", "456", "56088"), ("237", "284", "67308")]
    for qn in qns[:]:
        ans = Solution().multiply_inplace2(qn[0], qn[1])
        print(f"{qn[0]}x{qn[1]} ans={ans} sol={qn[2]}")
