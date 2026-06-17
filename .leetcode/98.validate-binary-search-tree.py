#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Time: 20 mins
    Pattern: MIN-Max Game, tree traversal
    Complexity: O(Nodes) Time, O(Nodes) Space
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, lo, hi):
            if not node:
                return True
            if lo is not None and node.val <= lo: 
                return False
            if hi is not None and node.val >= hi:
                return False
            return True and check(node.left, lo, min(node.val, hi) if hi else node.val) and check(node.right, max(lo, node.val) if lo else node.val, hi)
        return check(root, None, None)
# @lc code=end

