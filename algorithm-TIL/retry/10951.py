import sys

input=sys.stdin.readline

try:
    while 1:
        a,b=map(int,input().split())
        print(a+b)
except:
    exit()

    # 처음에 while문으로 true값 생각 못하다가 바로 생각나서 넣음