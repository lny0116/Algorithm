import sys

input=sys.stdin.readline

li = []
for i in range(3):
    n=int(input())
    li.append(n)

mul = li[0]*li[1]*li[2]
mul = str(mul)

for i in range(10):
    print(mul.count(str(i)))

# 결론적으론 안 보고 푼 거긴 한데, [count함수 구글링은 함]
# 근데 너무 잡고 풀고 있던 거라서, 다시 풀어보자