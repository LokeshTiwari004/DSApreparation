#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def napo(r, c):
            if 0 <= r < m and 0 <= c < n and grid[r][c]:
                grid[r][c] = 0
                return 1 + napo(r+1, c) + napo(r-1, c) + napo(r, c+1) + napo(r, c-1)
            return 0
        
        answer = 0
        for r in range(m):
            for c in range(n):
                answer = max(answer, napo(r, c))
        return answer
# @lc code=end

