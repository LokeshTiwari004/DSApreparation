#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
# Time: 30 mins
# Pattern: BFS
# Complexity: O(m*n) Time
# Edge Cases: Empty container, No fresh Oranges 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visiting = set()
        fresh_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    visiting.add((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        will_visit = set()
        minutes = -1
        while visiting:
            r, c = visiting.pop()
            if r < m-1 and  grid[r+1][c] == 1:
                grid[r+1][c] = 2
                will_visit.add((r+1, c))
                fresh_count -=1

            if r > 0 and  grid[r-1][c] == 1:
                grid[r-1][c] = 2
                will_visit.add((r-1, c))
                fresh_count -=1
            
            if c < n-1 and  grid[r][c+1] == 1:
                grid[r][c+1] = 2
                will_visit.add((r, c+1))
                fresh_count -=1
            
            if c > 0 and  grid[r][c-1] == 1:
                grid[r][c-1] = 2
                will_visit.add((r, c-1))
                fresh_count -=1
            
            if not visiting:
                minutes += 1
                visiting = will_visit
                will_visit = set()
        
        if fresh_count == 0:
            return minutes
        return -1
# @lc code=end