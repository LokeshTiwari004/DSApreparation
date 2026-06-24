#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from collections import deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        outgoing = dict()
        indegree = dict()
        max_iternary_size = 1
        for dep, arv in tickets:
            max_iternary_size += 1
            if dep in outgoing:
                outgoing[dep].append(arv)
            else:
                outgoing[dep] = [arv]
            
            indegree[arv] = indegree.get(arv, 0) + 1
        
        for dep in outgoing:
            outgoing[dep].sort(reverse=True)
        
        iternary = []
        # open = deque(iternary)
        open = ['JFK']
        while open:
            dep = open.pop()
            open.extend(outgoing[dep])
            iternary.append(dep)
            if outgoing[dep]:
                iternary.append(outgoing[dep].popleft())
            else:
                iternary.pop()
                outgoing[iternary[-1]].append(dep)
            print(outgoing)
        return iternary
# @lc code=end

