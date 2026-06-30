#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    """
    time: 30 mins
    hint: hint about the best solution
    time: O(n) time, O(n) space
    pattern: monotonic stack
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0 
        stack = [] # monotonic increasing stack
        for idx, height in enumerate(heights):
            while stack:
                if heights[stack[-1]] < height:
                    break
                else:
                    h = heights[stack.pop()]
                    if stack:
                        res = max(res, h * (idx - stack[-1] - 1))
                    else:
                        res = max(res, h * idx)
            stack.append(idx)
        
        while stack:
            h = heights[stack.pop()]
            if stack:
                res = max(res, h * (idx - stack[-1]))
            else:
                res = max(res, h * (idx+1))
        return res
# @lc code=end
