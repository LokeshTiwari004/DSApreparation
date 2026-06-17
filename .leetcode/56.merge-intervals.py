#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if not n:
            return []
        
        intervals.sort(key=lambda x:x[0])
        
        answer = [intervals[0]]

        for idx in range(1, n):
            item = intervals[idx]
            if item[0] <= answer[-1][1]:
                last = answer.pop()
                answer.append([min(last[0], item[0]), max(item[1], last[1])])
            else:
                answer.append(item)
        return answer

# @lc code=end

