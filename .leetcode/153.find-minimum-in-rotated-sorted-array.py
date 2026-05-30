#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    # """
    # Notes:
    # Time: 20 Mins
    # Hint: No
    # Pattern: Binary Search
    # Compleity: O(log n) time, O(1) space
    # Edge Case: no rotation, upper and lower ptrs adjacent, only two numbers in array
    # Reasoning: 
    #     Looking for Half region with leftmost index > rightmost index iteratively.
    # """
    def findMin(self, nums: List[int]) -> int:
        lower = 0
        upper = len(nums) - 1
        # min = None
        while True:
            cursor = lower + (upper - lower) // 2

            if cursor == lower:
                if nums[lower] < nums[upper]:
                    return nums[lower]
                else:
                    return nums[upper]

            if nums[lower] > nums[cursor]:
                upper = cursor
            elif nums[cursor] > nums[upper]:
                lower = cursor
            else:
                return nums[lower]

# @lc code=end

