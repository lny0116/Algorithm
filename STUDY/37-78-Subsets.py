# 68 ms	14.2 MB
# https://leetcode.com/problems/subsets/

def subsets(nums: list[int]) -> list[list[int]]:
    res = []

    dfs(nums, [], res)
    return res
    
def dfs(nums, path, res):
    res.append(path)
    for i in range(len(nums)): #[1,2,3] 기준 3 == i = 0,1,2
        dfs(nums[i+1:], path+[nums[i]], res)

print(subsets([1,2,3]))
print(subsets([0]))
