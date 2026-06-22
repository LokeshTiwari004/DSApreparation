#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ul = int((c // 2) ** 0.5)+1
        for i in range(ul):
            if ((c - i*i) ** 0.5).is_integer():
                return True
        return False
# @lc code=end

