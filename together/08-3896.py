# https://www.acmicpc.net/problem/3896

import sys
from math import sqrt

input = sys.stdin.readline

t = int(input())

def prime(num):
    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

front, back = 0, 0

for i in range(t):
    k = int(input())
    front = k
    back = k

    while prime(front) == False :
        front -= 1

    while prime(back) == False :
        back += 1
        
    print(back-front)


# 이거 이용 소수 구하는 함수를 만들래
#     for i in range(2, j):
#         res = True
#         if k % i == 0:
#             res = False

# 내 로직
# 먼저 해당 숫자의 앞 뒤 소수인 숫자를 출력해서 front, back값에 담고
# 그다음에