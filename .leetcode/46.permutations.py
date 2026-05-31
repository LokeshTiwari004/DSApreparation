#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
# Time: 30 Mins
# Hint:None
# Complexity: O(n!) time, O(n) space
# Pattern: Recursion
class Solution:
    def permutations(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            yield []
        
        for idx, num in enumerate(nums):
            first = [num]
            for rest in self.permutations(nums[:idx] + nums[idx+1:]):
                yield first + rest

    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for permuation in self.permutations(nums):
            answer.append(permuation)
        return answer
# @lc code=end

