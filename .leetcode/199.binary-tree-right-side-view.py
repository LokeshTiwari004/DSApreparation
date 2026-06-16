#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    """
    Time: 20 mins
    Pattern: Level Search BFS
    O(N) time O(N) space
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        current_lvl = deque([root] if root else [])
        next_lvl = deque()
        answer = []
        while current_lvl:
            node = current_lvl.popleft()
            if node.left:
                next_lvl.append(node.left)
            if node.right:
                next_lvl.append(node.right)
            
            if not current_lvl:
                current_lvl, next_lvl = next_lvl, current_lvl
                answer.append(node.val)
        return answer
# @lc code=end

