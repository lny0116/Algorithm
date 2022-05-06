# 4072 ms	14.9 MB
# https://leetcode.com/problems/two-sum
# 어제 풀었던 문제와 완전 동일하게 풀었음

def twoSum(nums: list[int], target: int) -> list[int]:
    l = len(nums)
    for i in range(l):
        for j in range(i+1, l): #여기 끝범위 줘야해
            sum = nums[i]+nums[j]
            if sum == target:
                return [i,j]


print(twoSum(nums = [2,7,11,15], target = 9))
print(twoSum(nums = [3,2,4], target = 6))
print(twoSum(nums = [3,3], target = 6))