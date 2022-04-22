import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    ox = input().strip() #문자열이라서 인덱스가 따로 저장된다 / list 안 써도 됨

    total=0
    num=0

    for j in ox: #2중 for문 또 못 함 ㅋㅋ
        if j == 'X':
            num = 0
            continue
        num += 1
        total += num

    print(total)

# 다시 한 번만 더 풀어보자~^^