#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        visiting = deque()
        visiting.append((root, 1))
        # print(visiting)
        level_order = dict()
        while visiting:
            node, level = visiting.popleft()
            if level in level_order:
                level_order[level].append(node.val)
            else:
                level_order[level] = [node.val]
            
            if node.left:
                visiting.append((node.left, level+1))
            if node.right:
                visiting.append((node.right, level+1))
        level = 1
        answer = []
        while level in level_order:
            answer.append(level_order[level])
            level +=1
        return answer
# @lc code=end

