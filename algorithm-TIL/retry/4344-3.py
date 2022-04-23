import sys

input = sys.stdin.readline

c = int(input())

for i in range(c):
    n = list(map(int,input().split()))
    avr = sum(n[1:])/n[0]

    cnt=0
    total =0
    for i in n[1:]:
        if i > avr:
            cnt+=1

    total = cnt/n[0]*100
    print(f'{total:.3f}%')

# 끝~!