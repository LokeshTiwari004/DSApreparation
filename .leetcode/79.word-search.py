#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board)-1, len(board[0])-1
        def trace(x, y, depth=0):
            if x < 0 or x > m or y < 0 or y > n or board[x][y] != word[depth]:
                return False
            return True and \
                (trace(x+1, y, depth+1) or \
                trace(x-1, y, depth+1) or \
                trace(x, y-1, depth+1) or \
                trace(x, y+1, depth+1))
        
        for i in range(m+1):
            for j in range(n+1):
                if trace(i, j):
                    return True
        return False
# @lc code=end

