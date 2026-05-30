#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    """
    20 mins
    no hints
    pattern: stack of integers
    complexity: o(n) time, o(n) space
    edge case: division bis zero truncated
    reasoning: 
        integers -> stack 
        operator -> unstack two interegrs -> operate -> stack result
        for negative quotient during divison:
            -> with remainder -> quotient + 1
            -> without remainder -> quotient
            
    """
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    stack.append( - stack.pop() + stack.pop())
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    a = stack.pop()
                    b = stack.pop()
                    c =  b // a
                    c = c+1 if c < 0 and b % a else c
                    stack.append(c)
                case _:
                    stack.append(int(token))
        return stack[0]
# @lc code=end

