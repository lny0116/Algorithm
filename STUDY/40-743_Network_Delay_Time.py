# 532 ms	16.5 MB
# https://leetcode.com/problems/network-delay-time/

from collections import defaultdict
import heapq


def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    graph = defaultdict(list)

    # 그래프 인접 리스트 구성
    for u, v, w in times:
        graph[u].append((v,w))

    # (소요시간, 정점)
    q = [(0,k)]
    
    dist = defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while q:
        time, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(q, (alt, v))

    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == n:
        return max(dist.values())
    
    return -1


print(networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)) # 2
print(networkDelayTime(times = [[1,2,1]], n = 2, k = 1)) # 1
print(networkDelayTime(times = [[1,2,1]], n = 2, k = 2)) # -1