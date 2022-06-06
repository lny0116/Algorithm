# 78 ms	13.9 MB
# https://leetcode.com/problems/permutations/


def permute(nums: list[int]) -> list[list[int]]:
    res = []
    dfs(nums, [], res)
    return res
    
def dfs(nums, path, res):
    if not nums:
        res.append(path)

    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)


print(permute([1,2,3]))
print(permute([0,1]))
print(permute([1]))

# 책 참고