#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        outdegree = {}
        incoming = {}
        for vertex in range(numCourses):
            outdegree[vertex] = 0
            incoming[vertex] = set()
        
        for a, b in prerequisites:
            incoming[b].add(a)
            outdegree[a] += 1
        
        zero_outdegree = [v for v, od in outdegree.items() if od == 0]
        course_schedule = []
        while zero_outdegree:
            item = zero_outdegree.pop()
            course_schedule.append(item)
            for dependent in incoming[item]:
                if outdegree[dependent] == 1:
                    outdegree.pop(dependent)
                    zero_outdegree.append(dependent)
                else:
                    outdegree[dependent] -= 1

        if len(course_schedule) != numCourses:
            return []
        return course_schedule
# @lc code=end

