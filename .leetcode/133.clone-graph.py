#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Time: 30 mins
# Hint: No
# Pattern: Graph Traversal
# complexity: O(Nodes) time, O(Nodes) space
# Edge Cases: Empty/singleton graph

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node or not node.neighbors:
            return node and Node(val=node.val)
        
        clone = dict()
        def traverse(node):
            if node.val in clone:
                return
            
            cp = Node(val=node.val)
            clone[node.val] = cp
            
            for neighbor in node.neighbors:
                traverse(neighbor)
                cp.neighbors.append(clone[neighbor.val])

        traverse(node)
        return clone[node.val]
            
# @lc code=end