import sys

input=sys.stdin.readline

n = int(input())

for i in range(n):
    ox = input().strip()

    cnt=0
    total=0
    for i in ox:
        if i == 'O':
            cnt+=1
            total+=cnt
        else:
            cnt=0
    print(total)

# ㅋㅋㅋㅋㅋㅋㅋ 진짜 돌겠네..
# else에서 자꾸 cnt+=0해서 틀리는거 진짜 에반데