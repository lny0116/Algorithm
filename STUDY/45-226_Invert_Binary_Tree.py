# 47 ms	13.9 MB
# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        
        # res = []

        while q:
            num = q.popleft()
            # print(num.val)
            
            if num:
                num.left, num.right = num.right, num.left
                # num.left.left, num.right.left = num.left.right, num.right.right
                
                q.append(num.right)
                q.append(num.left)
                
            
        return root