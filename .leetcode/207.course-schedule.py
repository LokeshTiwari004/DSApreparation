#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencyTree = dict()

        for c, p in prerequisites:
            if c in dependencyTree:
                dependencyTree[c].append(p)
            else: 
                dependencyTree[c] = [p]
        
        def haveCycle(c, seen=set()):
            if c not in dependencyTree:
                return False
            
            for p in dependencyTree[c]:
                if p in seen:
                    return True
                seen.add(p)
                if haveCycle(p, seen):
                    return True
                seen.remove(p)
            
            return False
        
        nocycle = set()
        for course in dependencyTree:
            if course in nocycle:
                continue
            if haveCycle(course):
                return False
            nocycle.add(course)
        return True
# @lc code=end
