# 331 ms	16.7 MB
# https://leetcode.com/problems/array-partition-i/

def arrayPairSum(nums: list[int]) -> int:
    l = len(nums)
    sum = 0
    mini = []
    nums.sort() # !!! 정렬을 하면 짝수번째가 무조건 2pair 기준 min이야

    # print(nums)

    for i in nums:
        # print(i) # 1,2,3,4
        mini.append(i) # for문 담은 i값 하나씩 담는데,
        if len(mini) == 2: #담은 게 길이가 2개가 되면
            sum += min(mini) #그거의 최소값을 sum에 담고
            mini = [] #mini 다시 초기화해서 다시 for문 돌리게
    
    return sum

    # 아래는 짝수번째가 무조건 min이라는 걸 깨닫고 푼 것

    # nums.sort()
    # return sum(nums[::2])


print(arrayPairSum([1,4,3,2]))
print(arrayPairSum([6,2,6,5,1,2]))