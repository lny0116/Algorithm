import sys

input=sys.stdin.readline

# def solve(a):
#     ans = print(sum(a))
#     return ans

# solve(list(map(int,input().split())))

# 어.. 이렇게 짜지 말고 양식이 있는데, 그 틀에 맞춰서 짜야함 ㄷ

def solve(a):
    ans =0
    for i in a:
        ans+=i
    return ans

# a=[1,2,3]
# print(solve(a))
# 이렇게 넣었을 때 돌아가게 작성해야하는거임..ㄷ... 어렵다~~
# 다시 풀자^^