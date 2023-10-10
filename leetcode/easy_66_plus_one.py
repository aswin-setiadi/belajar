class Solution:
    # 35.88% 49.48%
    def plusOne(self, digits: List[int]) -> List[int]:
        arr = digits[::-1]
        carry = 1
        for i in range(len(arr)):
            d_sum = arr[i] + carry
            arr[i] = d_sum % 10
            carry = d_sum // 10
            if i == len(arr) - 1:
                if carry != 0:
                    arr.append(carry)
        return arr[::-1]


# [1,2] will return [1,3], [9] will return [1,0]
