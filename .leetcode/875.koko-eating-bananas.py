#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#


# @lc code=start
class Solution:
    """
    15 Mins
    Pattern: Binary Search on Answer SPace
    O(log(max(piles))) Time
    O(1) space
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo , hi = 1, max(piles)
        while lo < hi:
            mid = (hi+lo) // 2
            time = 0
            for pile in piles:
                time += (pile + mid -1) // mid
            
            if time > h:
                lo = mid + 1
            else:
                hi = mid
        return (lo+hi) // 2
# @lc code=end