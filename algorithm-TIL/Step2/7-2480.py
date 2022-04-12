import sys

input=sys.stdin.readline

a,b,c=map(int, input().split())

if a==b==c:
    print(10000+(a*1000))
elif a==b:
    print(1000+(a*100))
elif a==c:
    print(1000+(a*100))
elif b==c:
    print(1000+(b*100))
else:
    print(max(a,b,c)*100)



# 내가 푼 식은 틀림 ㅋㅋ 다시 풀어보기

# if a==b==c:
#     print(10000+(a*1000))
# elif a != b != c:
#     if a>b:
#         print(a*100)
#     elif a>c:
#         print(a*100)
#     elif b>c:
#         print(b*100)
#     else:
#         print(c*100)

# if a==b and a !=c:
#     print(1000+(a*100))
# elif a==c and b!=c:
#     print(1000+(a*100))
# elif b==c and a!=b:
#     print(1000+(b*100))