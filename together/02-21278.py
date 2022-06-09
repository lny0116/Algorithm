# https://www.acmicpc.net/problem/21278
# https://hbj0209.tistory.com/50 + https://ryu-e.tistory.com/48 참고한 블로그

import sys
input = sys.stdin.readline

n,m= map(int, input().split()) #5개 건물 개수, 4개 도로

graph = [[1e9] * n for i in range(n)]

# 이거 과정이 모야?!
for i in range(m):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

# 모든 정점에서 모든 정점으로 가는 최단 거리 [플로이드 워셜]
for k in range(n):
    graph[k][k] = 0
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[j][k])

# 두 개의 건물을 선택해(치킨 집일 곳) 모든 집을 방문해서 걸리는 거리 측정
max = 1e9

for i in range(n-1): # 건물 두 개를 뽑아서
    for j in range(1,n):
        sum = 0
        for k in range(n): # 모든 집을 방문하면서 거리를 측정
            sum += min(graph[k][i], graph[k][j]) # 짧은 거리를 뽑아서 합쳐
        if max > sum*2:
            max = 2*sum
            res = [i+1, j+1, 2*sum]

print(*res) #unpacking이라는 데요 → 안 쓰면 [1,2,6] 이렇게 출력