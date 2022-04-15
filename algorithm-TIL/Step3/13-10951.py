import sys

input=sys.stdin.readline

while 1:
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        break

    # 확실한 것: try - except 문을 사용해야한다.
    # 난 이게 입력창이 열려있길래 잘못된줄알았는데.. 맞다네ㅋㅋ
    # 다 시 풀 기