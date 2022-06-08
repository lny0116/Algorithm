# 731 ms	15.8 MB
# https://leetcode.com/problems/combinations/

def combine(n: int, k: int):
        res = []
        dfs(list(range(1, n+1)), k, [], res)
        return res
    
def dfs(nums, k, path, res):
    if len(path) == k:
        res.append(path)
        return 
    for i in range(len(nums)):
        dfs(nums[i+1:], k, path+[nums[i]], res)


# def combine(n: int, k: int):
#     res = []

#     dfs(n,1,k)
#     resurn res

# def dfs(nums, start, k):
#     if k == 0:
#         res.append(nums[:])
#         resurn
    
#     for i in range(start, n+1):
#         nums.append(i)
#         dfs(nums, i+1, k-1)
#         nums.pop()
    


print(combine(4,2))
print(combine(1,1))