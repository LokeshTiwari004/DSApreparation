#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    # """
    # Notes: 
    # Time: 20 Mins
    # Hint: No
    # Pattern: Binary Search 
    # Complexity: O(log n) Time, O(1) space
    # Edge Cases: no rotation
    # """
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1
        while True:
            cursor = lower + (upper - lower) // 2
            if nums[lower] == target:
                return lower
            elif nums[upper] == target:
                return upper
            elif lower == cursor:
                return -1
            elif nums[lower] > nums[cursor]: 
                if nums[lower] > target and nums[cursor] < target:
                    lower = cursor
                else:
                    upper = cursor
            elif nums[cursor] > nums[upper]:
                if nums[cursor] > target and nums[upper] < target:
                    upper = cursor
                else:
                    lower = cursor 
            else:
                if nums[cursor] > target:
                    upper = cursor
                else:
                    lower = cursor

                    
# @lc code=end

