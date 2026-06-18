#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, maxdepth = len(board), len(board[0]), len(word)
        seen = set()
        def trace(x, y, depth):
            if depth == maxdepth:
                return True
            
            if not (-1 < x < m and -1 < y < n):
                return False
            
            id = x*n + y
            if id in seen:
                return False
            
            if board[x][y] == word[depth]:
                seen.add(id)
                if trace(x, y+1, depth+1) or trace(x+1, y, depth+1) or trace(x, y-1, depth+1) or trace(x-1, y, depth+1):
                    return True
                seen.remove(id)
            return False
        
        for i in range(m):
            for j in range(n):
                if trace(i, j, 0):
                    return True
        return False
# @lc code=end

