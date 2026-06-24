#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = root.val
        def DFS(node):
            left_max = DFS(node.left) if node.left else 0
            right_max = DFS(node.right) if node.right else 0
            self.max_path_sum =  max(
                self.max_path_sum, 
                left_max if node.left else self.max_path_sum, 
                right_max if node.right else self.max_path_sum,
                node.val, node.val + left_max + right_max)
            return node.val + max(left_max, right_max, 0)
        self.max_path_sum = max(DFS(root), self.max_path_sum)
        return self.max_path_sum
# @lc code=end

