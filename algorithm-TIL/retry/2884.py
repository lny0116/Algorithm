import sys

input=sys.stdin.readline

h,m=map(int,input().split())

if m>=45:
    print(h,m-45)
elif h>0 and m<45:
    print(h-1,m+15)
else:
    print(23,m+15)

    # 이거 틀렸었는데 그 이유가 7줄에 >만해서임... >= 이렇게 했었어야 했다...........
    # 45분과 같아도 45-45분=0분 할 수 있잖어..? ㅋㅋ