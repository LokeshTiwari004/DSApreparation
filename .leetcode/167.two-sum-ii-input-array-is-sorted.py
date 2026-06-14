#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for id, num in enumerate(numbers):
            if num in seen:
                return [seen[num]+1, id+1]
            seen[target-num] = id
# @lc code=end

