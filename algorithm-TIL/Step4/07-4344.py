import sys

input=sys.stdin.readline

c = int(input())

for i in range(c):
    n= list(map(int, input().split()))
    aver = sum(n[1:])/n[0]
    
    cnt = 0

    for j in n[1:]: #하나씩 뽑아서 
        if j>aver: #비교
            cnt+=1 #평균보다 높으면 +1
    total = cnt/n[0]*100 # 백분율
    print(f'{total:.3f}%') #{변수:.xf} 소수 몇자리까지 출력