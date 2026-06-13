#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: 20 min
# Hint: No
# Pattern: constraint based Tree traversal
# Complexity: O(height) Time, O(1) space 

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_val = min(p.val, q.val)
        max_val = p.val + q.val - min_val
        node = root 
        while node:
            if node.val < min_val:
                node = node.right
            elif node.val > max_val:
                node = node.left
            elif min_val < node.val < max_val or node.val == min_val or node.val == max_val:
                break
        return node
# @lc code=end

