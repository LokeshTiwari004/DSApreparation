#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        root = answer
        carry = 0
        while l1 or l2:
            addition = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            digit = addition % 10
            carry = addition // 10
            answer.next = ListNode(val=digit)
            answer, l1, l2 = answer.next, l1.next if l1 else None, l2.next if l2 else None
        if carry:
            answer.next = ListNode(val=carry)
        return root.next
# @lc code=end

