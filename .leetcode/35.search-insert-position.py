#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# Notes:
# Pattern: 
# 

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums)
        while True:
            cursor = lower + (upper - lower) // 2
            if cursor == lower:
                if nums[lower] >= target:
                    return lower
                else:
                    return upper
            elif nums[cursor] == target:
                return cursor
            elif nums[cursor] > target:
                upper = cursor
            else:
                lower = cursor

# @lc code=end

