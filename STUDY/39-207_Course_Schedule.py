# 150 ms 17.6 MB
# https://leetcode.com/problems/course-schedule/

from collections import defaultdict


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = defaultdict(list)
    #그래프 구성

    for a, b in prerequisites:
        graph[a].append(b)

    traced, visited = set(), set()

    def dfs(i):
        # 순환 구조이면 false
        if i in traced:
            return False
        # 이미 방문했던 노드이면 true
        if i in visited:
            return True
        
        traced.add(i)

        for b in graph[i]:
            if not dfs(b):
                return False
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        visited.add(i)

        return True

    for a in list(graph):
        if not dfs(a):
            return False

    return True

print(canFinish(2,[[1,0],[0,1]]))
print(canFinish(2,[[1,0]]))

# 책 참고