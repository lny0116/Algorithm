# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    
    # for i in computers:
    #     # print(i)
    #     for j in range(n-1):
    #         for k in range(1,n):
    #             if i[j] == i[k]:
    #                 answer = 1
    #             else:
    #                 answer +=1
    # 이상한 풀이 ㅋㅋㅋㅋ 테이스 케이스는 다 통과해서 설렜다^^..

    visited = [[] for i in range(n)] # [0, 0, 0]
    # 밑이랑 같은 코든데, 이렇게 바꿔봄
    # for i in range(n):
    #     visited.append(0)
        
    for idx in range(n):
        answer += dfs(idx, computers, visited)
                
    return answer

def dfs(idx, computers, visited):
    if visited[idx]: # 방문했던 곳이면 pass
        return 0
    else:
        visited[idx] = 1 # 방문 체크
        for i in range(len(computers)):
            if (computers[idx][i] == 1):
                dfs(i, computers, visited)
        return 1


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1
print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]])) # 1
