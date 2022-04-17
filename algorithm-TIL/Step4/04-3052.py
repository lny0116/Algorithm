import sys

input =sys.stdin.readline

# a=[]
# cnt=0
# for i in range(10):
#     n= int(input())
#     a.append(n%42)
#     sum = a.count(i)
#     cnt = len(sum)

# print(cnt)

# 내 구현... 근데 이렇게 안되더라고용(실패) 답지 참고함~

arr = []
for i in range(10):
    n=int(input())
    arr.append(n%42)

arr = set(arr)
print(len(arr))

# 서로 다른 나머지가 몇 개 있는지 출력 == 중복을 없애라는 건데, 이 작업도 안 해줬고..
# 그냥 마지막 2줄만 하면 되는건데, 저 생각을 못함 ㅋㅋ