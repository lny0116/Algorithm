#	102 ms	18.7 MB
# https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict


def topKFrequent(nums: list[int], k: int) -> list[int]:
    dic = defaultdict(int)

    for i in nums:
        dic[i] += 1

    dic_sort = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    res = []

    for key,value in dic_sort:
        # print(a,b)

        if len(res) < k:
            res.append(key)
    
    return res


print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(topKFrequent(nums = [1], k = 1))


'''
defaultdict(<class 'int'>, {1: 3, 2: 2, 3: 1})
dict_values([3, 2, 1])
dict_values([1])
'''
