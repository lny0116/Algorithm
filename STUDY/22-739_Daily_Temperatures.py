# 1854 ms	25.1 MB
# https://leetcode.com/problems/daily-temperatures/

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    l = len(temperatures)
    stack = []
    res = [0]*l

    for i in range(l):
        # 현재 온도가 스택 값보다 높다면 정답 처리 / stack에다가 현재 인덱스를 저장해두고
        while stack and temperatures[i] > temperatures[stack[-1]]: #stack[-1] == 맨 뒤
            res[stack[-1]] = i - stack[-1] # 해당 인덱스보다 큰 인덱스가 몇 번짼지 지금 i값과 빼서 res에 담음
            stack.pop() #이전 인덱스랑 현재 인덱스를 비교했으면, 이번엔 현재 인덱스 값을 저장해서 다음과 비교해야 해서 pop해줘서 비워줘
        stack.append(i) #그리고 이제 현재 인덱스를 넣어주고 반복~
    
    return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90]))
