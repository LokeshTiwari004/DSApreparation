#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# Notes:
#  - Pattern: Simple Binary Search
#  - Complexity: O(nlogn) time, O(1) space
#  - EdgeCases: when upper pt and lower pt same or adjacent


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1
        cursor = lower + (upper - lower) // 2
        while True:
            num = nums[cursor]
            if target > num:
                lower = cursor
            elif target < num:
                upper = cursor
            else:
                return cursor
            if upper - lower < 2:
                if nums[upper] == target:
                    return upper
                elif nums[lower] == target:
                    return lower
                else:
                    return -1
            cursor = lower + (upper - lower) // 2
# @lc code=end

