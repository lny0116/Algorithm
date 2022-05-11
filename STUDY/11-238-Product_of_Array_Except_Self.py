# 567 ms	42.4 MB
# https://leetcode.com/problems/product-of-array-except-self/
# 라이브러리 numpy를 썼는데... 이거 안되는...?

from numpy import multiply


def productExceptSelf(nums: list[int]) -> list[int]:
    front_mul = []
    back_mul = []
    init = 1
    l = len(nums)

    # front mul
    for i in range(l):
        front_mul.append(init)
        init *= nums[i]
    # print(front_mul)

    init = 1 # 여기서 한 번 더 초기화를 안 해주면, 24값이 들어가.. 왜..? ㅇ-ㅇ..
    # back mul
    for i in reversed(range(l)):
        back_mul.append(init)
        init *= nums[i]
    # print(back_mul[::-1])

    mul = list(multiply(front_mul, back_mul[::-1]))
    return mul



    # mul = 0
    # temp = []

    # l = len(nums)

    # for i in nums:
    #     a = nums.index(i)
    #     nums.pop(a)
    #     # temp.append(a)
    #     # mul *= i

    #     print(nums)



print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))

# 처음 생각했던 방법은, for문 돌려서 해당 인덱스들 pop으로 빼고, []에 남아있는 애들끼리
# 곱한 결과를 temp = []에 차곡차곡 담아서 output 내는걸로...!!! (시간초과가 난다는 소식을 듣고 접음)