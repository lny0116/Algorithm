import sys

input=sys.stdin.readline

a,b=map(int,input().split())
c=int(input())

a=(a+(b+c)//60)%24
b=(b+c)%60

print(a,b)

# 약간 외워서 푼 것 같은 기분인데.. 술술 막힘없이 외워서 입력ㅋㅋ