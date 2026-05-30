#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    """
    Time 10 mins
    No Hint
    Stack, Hashmap
    O(n) time, O(n) space
    Edge Case: non empty stack after loop, empty stack within loop
    """
    def isValid(self, s: str) -> bool:
        op = {'{', '[', '('}
        stack = []
        for b in s:
            if b in op:
                stack.append(b)
                continue
            if not stack:
                return False
            cl = stack.pop()
            if b == ')' and cl != '(':
                return False
            elif b == '}' and cl != "{":
                return False
            elif b == "]" and cl != "[":
                return False
        if stack:
            return False
        return True

# @lc code=end

