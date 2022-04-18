import sys

input=sys.stdin.readline

n=int(input())

for i in range(n):
    m = list(input().strip())
    sum = 0
    total = 0
    for j in m:
        if j == 'O':
            sum+=1
            total+=sum
        else:
            sum=0
    print(total)

    # if m[i] == 'O':
    #     sum+=
    # # else:
    # #     sum+=0

    # print(sum)
    # 내가 짠 코드.. 비슷한디, 내가 머리가 안 굴러갔음 ㅠㅠ
    # 다시풀기~