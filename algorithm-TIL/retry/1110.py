import sys
input=sys.stdin.readline

n= int(input())
num = n
cnt = 0

while 1:
    a = num//10 #앞글자 뱉음
    b= num%10 #뒷글자 뱉음
    c = (a+b)%10 #앞 뒤 더한 값 출력
    num = (b*10)+c #뒷글자+더한값을 더함

    cnt +=1

    if num == n:
        break

print(cnt)

# 다시 풀어봐야함