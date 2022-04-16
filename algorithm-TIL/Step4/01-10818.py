import sys
input=sys.stdin.readline

n=int(input())
nLi = list(map(int,input().split()))

print(f'{min(nLi)} {max(nLi)}')