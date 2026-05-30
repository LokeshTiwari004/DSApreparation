#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#


# @lc code=start
class Solution:
    """
    20 Mins
    Pattern: Binary Search with 
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (hi + lo) // 2
            t = 0
            for p in piles:
                t += (p + mid - 1) // mid
            if t > h:
                lo = mid + 1
            else:
                hi = mid
        return lo
# @lc code=end

