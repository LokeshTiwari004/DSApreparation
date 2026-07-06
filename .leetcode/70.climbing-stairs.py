#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start

# time: 10mins
# hint: no
# complexity: O(n) time O(1) space


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        a, b = 1, 2
        for _ in range(n-2):
            a, b = b, a+b
        return b
# @lc code=end

