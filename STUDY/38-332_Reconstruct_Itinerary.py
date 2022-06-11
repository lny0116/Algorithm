# 85 ms	14.6 MB
# https://leetcode.com/problems/reconstruct-itinerary/

from collections import defaultdict

def findItinerary(tickets: list[list[str]]) -> list[str]:
    graph = defaultdict(list)
    
    for i, v in sorted(tickets):
        graph[i].append(v)

    res = []

    def dfs(i):
        
        while graph[i]:
            dfs(graph[i].pop(0))
        res.append(i)

    dfs('JFK')

    return res[::-1]

        
#     res = []

#     dfs(tickets, "", res)
#     return res

# def dfs(air, path, res):
#     sort_air = sorted(air) #[["JFK","MUC"],["LHR","SFO"],["MUC","LHR"],["SFO","SJC"]]
    
#     # for i in range(len(sort_air)):
#     for i in sort_air:
#         if i[0] == 'JFK':
#             i[1]

print(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))

# 책 참고
