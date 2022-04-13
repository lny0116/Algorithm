import sys

input=sys.stdin.readline

t=int(input())

for i in range(t):
    a,b=map(int,input().split())
    print(a+b)

# 'int' object is not subscriptable
# 라는 오류가 계속 떴었는데, 내가 인덱스가 아닌 정수를 뽑아놓고 인덱스로 호출하려고 해서 ㅋㅋ
# 그래서 생각해보니 a랑 b를 그냥 더하면 되잖아? 해서 수정해서 성공시킴ㅎㅎ