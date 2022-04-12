# %연산과 //연산을 섞어주면 시계 연산이 가넝한
# 특히 %24 연산은 24시가 넘어갔을 떄 0으로 바꿔준다고 생각!

import sys

input=sys.stdin.readline

a,b=map(int,input().split())
c=int(input())

a=(a+(b+c)//60)%24
b=(b+c)%60

print(a,b)


# 다시 풀어야함ㅋㅋ

# if b+c<60:
#     print(a,(b+c)+c)
# else:
#     print(a+1,(b+c)-(60-c))