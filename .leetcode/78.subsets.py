#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
# Time: 10 mins
# Hint: None
# Pattern: Backtracking
# complexity: O(2^n) time, O(2^n) space
# Edge Case: empty set
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = [[]]
        for num in nums:
            new = []
            for set in power_set:
                new.append(set + [num])
            power_set.extend(new)
        return power_set
# @lc code=end

