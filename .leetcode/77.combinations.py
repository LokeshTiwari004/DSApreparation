#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
# Time: 5 mins
# Hint: None
# Pattern: BackTracking
# Complexity: O(n^k) time, O(n) space
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def backtrack(path, start, stop, k):
            if k == 0:
                answer.append(path)
                return
            elif stop - start + 1 < k:
                return
            backtrack(path + [start], start+1, stop, k -1)
            backtrack(path, start+1, stop, k)
        backtrack([], 1, n, k)
        return answer
# @lc code=end

