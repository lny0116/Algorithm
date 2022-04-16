import sys

input=sys.stdin.readline

while 1:
    a,b=map(int,input().split())
    if a!=0 and b!=0:
        print(a+b)
    else:
        break

    # 굿 처음에 a,b 변수를 위에다 넣어야 하는 거 생각못햇다가 바로 함