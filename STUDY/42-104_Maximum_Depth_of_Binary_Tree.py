# 62 ms	15.3 MB
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 예외처리 안 해주면 시간초과

# Definition for a binary tree node.

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        
        if not root:
            return 0
        
        depth = 0

        while q:
            depth += 1
            
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return depth

# p = self(root = [3,9,20,None,None,15,7])

print(Solution.maxDepth(root = [3,9,20,None,None,15,7]))
print(Solution.maxDepth([1,None,2]))

# 이거 어떻게 프린트 찍어보나요...?ㅠㅠ self의 문젠가요...