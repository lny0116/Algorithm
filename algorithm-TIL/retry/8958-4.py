import sys

input=sys.stdin.readline

n = int(input())
for i in range(n):
    m = input().strip()

    total=0
    cnt=0
    for j in m:
        # cnt=0
        if j =='O':
            cnt+=1
            total+=cnt
        else:
            cnt=0

    print(total)

# ㅋㅋ 진짜 머리 안 돌아가나ㅠㅠ
# 다시 풀어라^^