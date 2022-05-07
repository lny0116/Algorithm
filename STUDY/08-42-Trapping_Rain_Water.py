# 204 ms	15.8 MB
# https://leetcode.com/problems/trapping-rain-water/
# 계속 틀려서 결국 답지 보고 품 ㅠㅠ

def trap(height: list[int]) -> int:
    if height == []: #리스트에 값이 없으면
        return 0
    
    l = len(height)
    cnt, start, end = 0, 0, l-1
    left, right = height[start], height[end]
    
    while start < end: #최대 지점에서 좌우 포인터가 서로 만남
        left, right = max(height[start], left), max(height[end], right)

        if left <= right: #최대와 현재의 차이만큼 물 높이를 더함
            cnt += left - height[start]
            start += 1

        else: #왼쪽이 크면
            cnt += right - height[end]
            end -=1

    return cnt


print(trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])) #6
print(trap(height = [4,2,0,3,2,5])) #9