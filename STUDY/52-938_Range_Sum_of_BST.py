# 289 ms	22.9 MB
# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.ans += node.val
                    #print(node.val)
                    
                if node.val>low:
                    dfs(node.left)
                    
                if node.val<high:
                    dfs(node.right)
                    
        self.ans = 0
        
        dfs(root)
        
        return self.ans
