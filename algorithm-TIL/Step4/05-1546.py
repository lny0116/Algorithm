import sys

input = sys.stdin.readline

n=int(input())
m=list(map(int,input().split()))

maxi = max(m)

newCal = []
for i in range(len(m)):
    newCal.append(m[i]/maxi*100)


print(sum(newCal)/len(newCal))