#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
# Time: 30 mins
# Hint: None
# Pattern: Backtracking
# complexity: O(n^target) Time, O(n*target) space
# Reasoning: Select one numebr( in out case last num) 0 or more times only then move to next num
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def backtrack(path, remaining, target):
            if target == 0:
                answer.append(path)
                return
            elif target < 0:
                return
            elif not remaining:
                return
            last = remaining[-1]
            backtrack(path + [last], remaining, target - last)
            backtrack(path, remaining[:-1], target)
        backtrack([], candidates, target)
        return answer

# @lc code=end

