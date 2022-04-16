import sys

input = sys.stdin.readline

li=[]
for i in range(9):
    n = int(input())
    li.append(n)

m = max(li)

print(m)
print(li.index(m)+1) #인덱스 값에 +1해야지 시각적인 순번으로 출력

# 원하는 인덱스 값 찾는 거를 몰라서 찾아서 풀었음 구글링으로~