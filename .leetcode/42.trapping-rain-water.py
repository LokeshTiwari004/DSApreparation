#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==0:
            return 0

        leftmax = [0] * n
        rightmax = [0] * n

        leftmax[0] = height[0]
        rightmax[-1] = height[-1]

        for i in range(1, n):
            leftmax[i] = max(leftmax[i-1], height[i])
            rightmax[n-i-1] = max(rightmax[n-i], height[n-i-1])
        
        res = 0
        for i in range(n):
            res += min(leftmax[i], rightmax[i]) - height[i]
        return res
# @lc code=end

