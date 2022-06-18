# 	436 ms	18.1 MB
# https://leetcode.com/problems/longest-univalue-path/

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    res = 0 #여기다가 넣어줘야 오류가 안 나네..?
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            
            if not node:
                return 0
            
            # 존재하지 않는 노드까지 재귀적으로 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 현재 노드가 자식 노드와 동일한 경우 거리 1증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
                
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            
            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
            self.res = max(self.res, left + right)
               
            # 자식 노드 상태값 중 큰 값 반환
            return max(left, right)
        
        dfs(root)
        
        return self.res