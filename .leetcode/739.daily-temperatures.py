#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    """
    20 Mins
    No Hint
    Pattern: stacks
    Complexity: O(n) time, O(n) space
    Edge Case: when tmeprature is constant for days
    Reasoning: stacking non-increasing trend -> unstacking when trend breaks
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = len(temperatures)
        answer = [0] * days
        stack = []
        cursor = 0
        while cursor < days:
            if stack and temperatures[cursor] > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = cursor - last
            else:
                stack.append(cursor)
                cursor+=1
        return answer
# @lc code=end

