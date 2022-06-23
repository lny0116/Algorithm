# 	904 ms	24.9 MB
# https://leetcode.com/problems/minimum-height-trees/

from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # print(graph)

        leaf = []

        for i in range(n+1):
            if len(graph[i]) == 1:
                leaf.append(i)
        
        while n>2: #최종 2개가 남을 때까지 반복해야 함 / root... hmm
            n -= len(leaf)
            
            leaves = []
            
            for l in leaf:
                around = graph[l].pop()
                graph[around].remove(l)
                
                if len(graph[around]) == 1:
                    leaves.append(around)
                    
            leaf = leaves
                
        return leaf