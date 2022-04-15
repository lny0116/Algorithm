import sys

input=sys.stdin.readline

while 1:
    a,b=map(int,input().split())
    if a!=0 and b!=0:
        print(a+b)
    else:
        break

    # 답지봄 ㅎ
    # 이게 while 문을 통해 1(true)일때 계속 입력을 받고, 마지막에 0값이 들어오면 멈추게 하는거더라