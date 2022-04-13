import sys

input=sys.stdin.readline

n=int(input())

# range(start, stop, step) >>> step에 숫자 -1을 입력하면 start~stop까지 수를 줄이면서 출력
# n,0 >> 5,0 >> 5~1까지
for i in range(n,0,-1):
    print(i)

# 다시풀기 ㅋ