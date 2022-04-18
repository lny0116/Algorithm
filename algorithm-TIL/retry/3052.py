import sys

input=sys.stdin.readline

li = []
for i in range(10):
    n = int(input())
    mod = n%42
    li.append(mod)

print(len(set(li)))

#  크~ 풀어ㄸㅏ~