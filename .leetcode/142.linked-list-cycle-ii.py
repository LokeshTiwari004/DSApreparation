#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Time: 30 Mins
# Hint: Yes
# Pattern: Fast/Slow Pointer
# Complexity: O(n) time, O(1) space
# Edge Cases: Cycle Begins at 0
# Reasoning:

#         let cycle begin at index s and cycle has k nodes.
#         Then after t iterations 
#             slow: t if t < s else s + (t-s)%k
#             fast: 2t if 2t < s else s + (2t-s)%k  
        # if cycle exits 
        # then there exists t>=s 
        # such that slow = fast i.e. s + (t-s)%k = s +(2t-s)%k
        # solving we get t=2t(mod k) => t=0(mod k)

        # let fast = slow for t = kp >= s
        
        # let s = kq+r where  0 < r < k 
        # then slow = s + k - r = fast
        # then if we move any one ptr to 0-index and move both pt one step for s itertaion
        # then 0-ptr moves to s
        # and other ptr = s + (s + k - r + (kq + r) - s)%k = s
        # both meet at s

        # let s = kq
        # then slow = s and fast = s
        # but we do not know this at run time
        # so one pt moves to 0-index and then both move one node for s iterations
        # both pt become s.



class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        fast = head
        slow = head
        flag = True
        while True:
            slow = slow.next
            fast = fast.next

            if not fast or not slow:
                return None
            
            if flag:
                if fast.next:
                    fast = fast.next 
            
                if fast == slow:
                    if fast == head:
                        return head
                    fast = head
                    flag = False
            elif fast == slow:
                return fast
# @lc code=end

