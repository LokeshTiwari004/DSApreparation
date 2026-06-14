#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for id, num in enumerate(nums):
            if id > max_reachable:
                return False
            max_reachable = max(max_reachable, id+num)
        return True
# @lc code=end

