#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        mr, mc = len(grid), len(grid[0])
        def eatIsland(r, c):
            if 0 <= r < mr and 0 <= c < mc and grid[r][c]=='1':
                grid[r][c] = '0'
                eatIsland(r, c-1)
                eatIsland(r, c+1)
                eatIsland(r+1, c)
                eatIsland(r-1, c)
        
        current = deque([(0, 0)])
        next = deque()
        answer = 0
        while current or next:
            r, c = current.popleft()
            if grid[r][c]=='1':
                eatIsland(r, c)
                print()
                answer+=1

            if not next and c < mc - 1:
                next.append((r, c+1))
            if r < mr - 1:
                next.append((r+1, c))

            if not current:
                current, next = next, current
        return answer 



# @lc code=end

