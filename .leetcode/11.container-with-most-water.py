#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        res = 0
        while lo < hi:
            lh = height[lo]
            rh = height[hi]
            if lh < rh:
                res = max(res, lh * (hi - lo))
                lo += 1
            else:
                res = max(res, rh * (hi - lo))
                hi -= 1
        return res

# @lc code=end

