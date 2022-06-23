# 180 ms	15.3 MB
# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            # print(root1.val, root2.val)
            tree = TreeNode(root1.val + root2.val)
            
            tree.left = self.mergeTrees(root1.left, root2.left)
            tree.right = self.mergeTrees(root1.right, root2.right)
            
            # print(tree.left, tree.right)
            return tree
        else:
            return root1 or root2