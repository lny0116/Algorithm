import sys

input=sys.stdin.readline

h,m = map(int,input().split())

if m>=45:
    print(h,m-45)
elif h>0 and m<45:
    print(h-1,m+15)
else:
    print(23,m+15)

    # 굿ㅋㅋ 외워진 거 아닌가 이정도면... 암튼 풀었다