# 52 ms	13.8 MB
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0
        stack = []
        n = root
        
        while n or stack:
            if not n:
                n = stack.pop()
            else:
                while n.right:
                    stack.append(n)
                    n = n.right
            total += n.val
            n.val = total
            n = n.left
        return root
