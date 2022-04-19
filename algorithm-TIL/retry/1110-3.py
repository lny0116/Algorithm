import sys

input=sys.stdin.readline

n=int(input())
num= n
sum = 0

while 1:
    a=num//10 #2
    b=num%10 #6
    c=(a+b)%10
    num = (b*10)+c

    sum+=1

    if num == n:
        break

print(sum)

# 약간 외워진 것 아닌가... 항상 의문이지만 풀긴 풀었다는 것...ㄷ..