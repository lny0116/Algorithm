import sys
input=sys.stdin.readline

n=int(input())

for i in range(n):
    li = list(input().strip()) #하나씩 쪼개져서 들간다

    sum =0
    total = 0

    for j in li:
        if j == 'O':
            sum+=1
            total+=sum
        else:
            sum=0
    print(total)


# cnt =0
# for j in li:
#     if j in 'O':
#         cnt+=1
#     else:
#         cnt+=0

# print(cnt)


# 다시 풀기^^......