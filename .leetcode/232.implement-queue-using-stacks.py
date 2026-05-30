#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:
    """
    20 mins
    No Hint
    Pattern: unstack the pile into another stack
    Complexity: O(n) time, O(n) space
    """
    def __init__(self):
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        while self.second:
            self.first.append(self.second.pop())
        self.first.append(x)

    def pop(self) -> int:
        while self.first:
            self.second.append(self.first.pop())
        return self.second.pop()


    def peek(self) -> int:
        while self.first:
            self.second.append(self.first.pop())
        return self.second[-1]

    def empty(self) -> bool:
        return not bool(self.first or self.second)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

