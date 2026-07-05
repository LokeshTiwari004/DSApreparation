#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start

# time: 10mins
# hint: no
# complexity: O(n^2) time O(1) space


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
# @lc code=end

