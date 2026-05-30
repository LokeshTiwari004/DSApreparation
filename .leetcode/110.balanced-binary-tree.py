#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Time: 40 mins
# Hint: Studied Height balanced tree from gfg
# Pattern: Recursive-height-balance-check
# Complexity: O(nodes) time, O(height) space
# Edge Case: Empty Tree is also height balanced
class Solution:
    def height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left_h = self.height(node.left)
        right_h = self.height(node.right)
        
        if not (-2 < right_h - left_h < 2):
            self.balanced = False 
        
        return 1 + left_h if left_h > right_h else 1 + right_h
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.height(root)
        return self.balanced
# @lc code=end

