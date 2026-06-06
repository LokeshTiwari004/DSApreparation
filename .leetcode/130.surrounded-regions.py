#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def surrounded(x, y):
            visiting = {(x, y)}
            visited = set()
            while visiting:
                pt = visiting.pop()
                visited.add(pt)
                
                x, y = pt
                adj = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                
                for pt in adj:
                    x, y = pt

                    if x==-1 or x==m or y==-1 or y==n:
                        return
    
                    if board[x][y] == 'X' or pt in visited:
                        continue


                    if pt not in visiting:
                        visiting.add(pt)
                    
            for x, y in visited:
                board[x][y] = 'X'
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    surrounded(i, j)
# @lc code=end

