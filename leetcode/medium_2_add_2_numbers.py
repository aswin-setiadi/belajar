import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: None = None):
        self.val = val
        self.next = next


class Solution:
    # speed 6.83%, memory 82.56%
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nums: list[int] = []
        for v in [l1, l2]:
            _: list[str] = []
            while True:
                _.append(str(v.val))
                if not v.next:
                    tmp_int = int("".join(reversed(_)))
                    nums.append(tmp_int)
                    break
                v = v.next
        print(nums)
        ans = str(sum(nums))[::-1]
        print(ans)
        n = ListNode()
        tmp = n
        for d in ans[:-1]:
            print(d)
            tmp.val = int(d)
            tmp.next = ListNode()
            tmp = tmp.next
        tmp.val = int(ans[-1])
        return n

    @staticmethod
    def list_to_linked_list(l: list[int]) -> ListNode:
        head = ListNode(l[0])
        cursor = head
        for item in l[1:]:
            cursor.next = ListNode()
            cursor = cursor.next
            cursor.val = item
        return head

    @staticmethod
    def linked_list_to_list(ll: ListNode) -> list[int]:
        cursor = ll
        tmp_l: list[int] = []
        while cursor is not None:
            tmp_l.append(cursor.val)
            cursor = cursor.next
        return tmp_l


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        loop while node cursor is ListNode for both or carry exist
        first carry is 0
        """
        cursor1 = l1
        cursor2 = l2
        carry = 0
        dummy_head = ListNode()
        ans_cursor = dummy_head
        while cursor1 or cursor2 or carry != 0:
            if cursor1 is None:
                v1 = 0
            else:
                v1 = cursor1.val
            if cursor2 is None:
                v2 = 0
            else:
                v2 = cursor2.val
            total = v1 + v2 + carry
            current_digit = total % 10
            carry = total // 10
            ans_cursor.next = ListNode(current_digit)
            ans_cursor = ans_cursor.next
            cursor1 = cursor1.next if cursor1 is not None else None
            cursor2 = cursor2.next if cursor2 is not None else None
        return dummy_head.next


class TestSolution(unittest.TestCase):
    def test_sample(self):
        # Explanation: 342 + 465 = 807.
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        output = [7, 0, 8]
        ll1 = Solution.list_to_linked_list(l1)
        ll2 = Solution.list_to_linked_list(l2)
        ans_ll = Solution2().addTwoNumbers(ll1, ll2)
        output = Solution.linked_list_to_list(ans_ll)
        self.assertEqual(Solution.linked_list_to_list(ans_ll), output)


def main():
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    output = [7, 0, 8]
    ll1 = Solution.list_to_linked_list(l1)
    ll2 = Solution.list_to_linked_list(l2)
    ans_ll = Solution2().addTwoNumbers(ll1, ll2)
    output = Solution.linked_list_to_list(ans_ll)
    print(output)


if __name__ == "__main__":
    # unittest.main()
    main()
