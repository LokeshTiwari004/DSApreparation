#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
# Time: 10 mins
# pattern: two pointer
# o(n) time and O(1) space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pt1, pt2 = 0, len(numbers)-1
        while pt1 < pt2:
            current = numbers[pt1] + numbers[pt2]
            if current == target:
                return [pt1+1, pt2+1]
            elif current > target:
                pt2 -= 1
            else:
                pt1 += 1
# @lc code=end