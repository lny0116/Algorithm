# 201 ms	15.2 MB
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# visited check 안 해주면 시간 초과 납니다~

from collections import defaultdict
import heapq

def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    graph = defaultdict(list)

    for start, end, price in flights:
        graph[start].append((end, price))
        # print(graph)
    
    # queue: [(가격, 정점, 남은 경유지 수)]
    q = [(0, src, k+1)]
    visited = [0]*n

    # 도착점까지 최소 비용 판별
    while q:
        price, node, k = heapq.heappop(q)
        if node == dst:
            return price
        if visited[node] >= k:
            continue
        visited[node] = k
        for v, w in graph[node]:
            alt = price + w
            heapq.heappush(q, (alt, v, k-1))

    return -1


print(findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
print(findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))
print(findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0))