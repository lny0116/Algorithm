# 98 ms	13.9 MB
# https://leetcode.com/problems/combination-sum/

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    dfs(candidates, target, [], res)
    return res

def dfs(idx, target, path, res):
    # for i in range(len(idx)):
    #     for j in idx[i]:
    #         if j or j+i == target:
    #             res.append(path)
    #             return
    if target < 0:
        return
    
    if target == 0:
        res.append(path)
        return
    
    for i in range(len(idx)):
        dfs(idx[i:], target-idx[i], path+[idx[i]], res)

print(combinationSum(candidates = [2,3,6,7], target = 7))
print(combinationSum(candidates = [2,3,5], target = 8))
print(combinationSum(candidates = [2], target = 1))