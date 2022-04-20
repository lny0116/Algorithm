import sys

input=sys.stdin.readline

n=int(input())

for i in range(n):
    m=list(input().strip()) #list로 담으면 문자열이 하나씩 리스트에 담김
    #['O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'X']

    sum=0
    total=0

    for i in m[0:]:
        if i == 'O':
            sum+=1
            total+=sum
        else:
            sum=0

    print(total)

# 일단 내가 짠 코드가 다 맞긴 했는데, 뭐가 틀렸냐면, for문을 2중으로해서 값을 출력해야 나오는건데,
# 그걸 파악 못 하고 다른 for문으로 돌리고 있었음..
# 생각하면서 짜라~~~~~~~ 하오아와앙ㄱ 