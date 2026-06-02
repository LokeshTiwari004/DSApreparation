#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
# Time: 5 mins
# Hint: None
# complexity:
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtrack(path, n, open):
            if open == 0 and n == 0:
                answer.append(path)
                return

            if open:
                backtrack(path+')', n, open-1)
            if n:
                backtrack(path+'(', n-1, open+1)

        backtrack('', n, 0)
        return answer
# @lc code=end

