#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    """
    time: 30 mins, with no ides to improve from brute
    hint: studied the solution
    time: O(4n) time, O(3n) space
    pattern: monotonic stack
    note: "next up learn on pass best solution"
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        widths = [1] * n
        left = [] # left monotonic stack
        right = [] # right monotonic stack
        for i in range(n):
            current_h = heights[i]
            left_bound = -1
            while left:
                if heights[left[-1]] < current_h:
                    left_bound = left[-1]
                    break
                left.pop()
            left.append(i)
            widths[i] += i - left_bound - 1

            current_h = heights[n-i-1]
            right_bound = n
            while right:
                if heights[right[-1]] < current_h:
                    right_bound = right[-1]
                    break
                right.pop()
            right.append(n-i-1)
            widths[n-i-1] += right_bound - (n-i-1) - 1

        res = 0
        for i in range(n):
            res = max(res, heights[i] * widths[i])
        return res

# @lc code=end
