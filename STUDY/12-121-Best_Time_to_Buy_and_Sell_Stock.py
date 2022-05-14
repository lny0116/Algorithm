# 1859 ms	25 MB
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import sys

def maxProfit(prices: list[int]) -> int:
    high = 0 #최대값을 구하려면 최소를 넣어주고 (어차피 0보다 크니까 0넣어줌!)
    low = sys.maxsize #최소값을 구하려면 최대값을 넣어주고

    for i in prices:
        high = max(high, i-low)
        low = min(low, i)

    return high


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

# 8줄 초반에 음수니까(i-low) 0 미만이면 값이 안 담기다가(max가 0이니까),
# min값이 뽑혀서 들어갔을때부터 돌아감
