#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# time: 10 mins
# hint: no
# pattern: recursion, binary-tree-inversion
# complexity: O(n) time, O(n) space
# edge-cases: empty tree
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
# @lc code=end

