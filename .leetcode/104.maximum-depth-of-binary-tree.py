#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.

# time: 10 mins
# hint: no
# pattern: recursive-tree-depth
# complexity: o(n) time, o(h) space
# edge case: empty tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# @lc code=end

