import sys

input=sys.stdin.readline

n = int(input())
num=list(map(int,input().strip()))
# [5, 4, 3, 2, 1]

print(sum(num))