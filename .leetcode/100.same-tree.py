#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Time: 20 mins
# Hint: No
# Pattern: Recursive-Tree-Traversal / Tree Comparison
# complexity: O(n) time, O(n) space
# Base Case: only one   TREE NODE is none, both none
# EdgeCase: Empty trees
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None) ^ (q is None):
            return False
        elif p is None and q is None:
            return True
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# @lc code=end