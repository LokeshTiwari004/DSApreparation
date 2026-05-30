#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
class Solution:
    """
    Time: 25 mins
    Hint: nO
    Pattern: Merge Sorted LL
    Complexity: O(n) time and O(n) space
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            sorted = list1
            current = list1
            list1 = list1.next
        else:
            sorted = list2
            current = list2
            list2 = list2.next
        while True:
            if list1:
                if list2 is None or list1.val < list2.val:
                    current.next, current = list1, list1
                    list1 = list1.next
                else:
                    current.next, current = list2, list2
                    list2 = list2.next
            elif list2:
                current.next, current = list2, list2
                list2 = list2.next
            else:
                break
        return sorted

# @lc code=end

