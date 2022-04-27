import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    ox = input().strip()

    cnt =0
    total=0
    for j in ox:
        if j == 'O':
            cnt+=1
            total+=cnt
        else:
            cnt=0
    
    print(total)

# ㅠㅠ 6트만에 탈출 ㅋㅋㅋ ㅠㅠ