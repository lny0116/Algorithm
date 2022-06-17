# 60 ms	16.4 MB
# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            nonlocal diameter

            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            diameter = max(diameter, left + right)

            return max(left, right) + 1
        
        diameter = 0
        height(root)
        
        return diameter


print(Solution.diameterOfBinaryTree([1,2,3,4,5]))
print(Solution.diameterOfBinaryTree([1,2]))

# https://www.daleseo.com/python-global-nonlocal/ [ nonlocal에 대해 ]