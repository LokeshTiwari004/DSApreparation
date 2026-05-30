#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        cursor = head
        lagged = head
        lag = 0
        while True:
            cursor = cursor.next
            
            if not cursor:
                break

            if lag == n:
                lagged = lagged.next
            else:
                lag += 1

        if lag == n - 1:
            head = head.next
        elif lag == n:
            lagged.next = lagged.next.next

        return head

# @lc code=end

