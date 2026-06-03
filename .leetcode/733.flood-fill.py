#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
# Time: 20 mins
# Hint: None
# Pattern: DFS/Recursion
# Complexity: O(M*N) time, O(M*N) space
# Key Idea:
# Graph traversal using DFS to fill connected components of identical pixel values.
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        base = image[sr][sc]
        if base == color:
            return image
        
        m, n = len(image), len(image[0])
        def DFS(r, c):
            if 0 <= r < m and 0 <= c < n and image[r][c] == base:
                image[r][c] = color
            
                DFS(r-1, c)
                DFS(r, c-1)
                DFS(r+1, c)
                DFS(r, c+1)
        
        DFS(sr, sc)
        return image
# @lc code=end

