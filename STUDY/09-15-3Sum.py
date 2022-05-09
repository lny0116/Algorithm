# 775 ms	18.2 MB
# https://leetcode.com/problems/3sum/
# 브루트 포스로 풀다가, 반례를 생각 못 하고 틀려서 답지 보고 풀었습니다 ㅠ^ㅜ
# 이거 투 포인터 풀이임, 완탐으로 풀면 시간초과 나

def threeSum(nums: list[int]) -> list[list[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀가며 합 sum 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0인 경우이므로 정답 및 스킵 처리
                results.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results



    # l = len(nums)

    # sum = []

    # # print(nums)

    # for i in range(l - 1):
    #         for j in range(i + 1, l - 1):
    #             for k in range(j + 1, l - 1):
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     if sorted([nums[i], nums[j], nums[k]]) in sum:
    #                         continue
    #                     sum.append([nums[i], nums[j], nums[k]])

    # return sum      





print(threeSum(nums = [-1,0,1,2,-1,-4])) #[[-1,-1,2],[-1,0,1]]
print(threeSum(nums = [])) #[]
print(threeSum(nums = [0])) #[]
print(threeSum(nums = [0,0,0])) #[[0,0,0]]
