#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import deque
class Solution:
    """
        Time: 30 mins after study
        Hint: YES, learned  "BFS-based topological sort" from agents
        Pattern: Kahn' Algorithm / BFS Topological Sort / Source Removal 
        Complexity: O(N+E) Time and Space  # O(N²) in the worst-case dense graph
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        outdegree = dict()
        incoming = dict()
        for i in range(numCourses):
            outdegree[i] = 0
            incoming[i] = set()

        for c, p in prerequisites:
            outdegree[c] += 1
            incoming[p].add(c)
        
        zerooutdegree = deque()
        for i in range(numCourses):
            if not outdegree[i]:
                zerooutdegree.append(i)
        
        while zerooutdegree:
            for vertex in incoming[zerooutdegree.popleft()]:
                outdegree[vertex] -= 1
                if outdegree[vertex] == 0:
                    zerooutdegree.append(vertex)

        for outdeg in outdegree.values():
            if outdeg:
                return False
        return True
# @lc code=end
