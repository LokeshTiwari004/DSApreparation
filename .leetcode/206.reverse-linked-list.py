#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.

class Solution:
    """
    Time: 20 mins
    Hint: No
    Pattern: swap var
    Coplexity: O(n) time, O(1) space
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        current = head
        while current:
            current.next, last, current = last, current, current.next
        return last
# @lc code=end

