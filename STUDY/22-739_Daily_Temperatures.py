# 1854 ms	25.1 MB
# https://leetcode.com/problems/daily-temperatures/

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    l = len(temperatures)
    stack = []
    res = [0]*l

    for i in range(l):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while stack and temperatures[i] > temperatures[stack[-1]]:
            res[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    
    return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90]))