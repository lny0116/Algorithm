# 수학적 문제인 것 같은데, 어떻게 식을 써야할지 감이 안 잡힘
# 답지 봄 https://elrion018.tistory.com/39
# 문자열로 풀 순 있긴 한데 시간초과가 나온다고.. int로 푼다!
import sys

input=sys.stdin.readline

n = int(input()) #55
num=n #55
cnt= 0

while 1:
    a = num//10 #5
    b= num%10 #5
    c= (a+b)%10 #0
    num = (b*10)+c #50+5=55

    cnt +=1
    if num == n: #숫자가 같다면 멈추게
        break

print(cnt)