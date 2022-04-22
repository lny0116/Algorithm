import sys

input=sys.stdin.readline

c =int(input())

for i in range(c):
    n = list(map(int,input().split()))
    avr = sum(n[1:])/n[0]
    
    cnt=0
    for j in n[1:]: #ㅋㅋ 이게 문제네 ㅎ 0인덱스 필요없잖아..
        if j > avr:
            cnt+=1

    total = cnt/n[0]*100
    print(f'{total:.3f}%')

# 한 번만 더 풀면 이제 잘 하지 않을까?
# 다 짰는데, 12줄만 헷갈린거니까..