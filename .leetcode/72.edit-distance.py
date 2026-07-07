#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a, b = len(word1), len(word2)
        lookup = dict()
        def dp(i=0, j=0):
            if (i, j) in lookup:
                return lookup[(i, j)]
            if i == a:
                lookup[(i, j)] = b-j
            elif j == b:
                lookup[(i, j)] = a-i
            elif word1[i] == word2[j]:
                lookup[(i, j)] = dp(i+1, j+1)
            else:
                lookup[(i, j)] = 1 + min(dp(i+1, j), dp(i, j+1), dp(i+1, j+1))
            return lookup[(i, j)]
        dp()
        return lookup[(0, 0)]
# @lc code=end

