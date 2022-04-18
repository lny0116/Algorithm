import sys

input=sys.stdin.readline

n=int(input())
num = n
cnt=0

while 1:
    a= num//10 #front
    b= num%10 # back
    c= (a+b)%10 #sum
    num = (b*10)+c
    #10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고

    cnt+=1

    if num == n:
        break
print(cnt)

# 다시풀기..ㅎ