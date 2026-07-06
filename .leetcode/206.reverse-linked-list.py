#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        while head:
            head.next , head, last = last, head.next, head
        return last
# @lc code=end

