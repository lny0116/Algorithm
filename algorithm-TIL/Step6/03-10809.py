import sys

input = sys.stdin.readline

s= input().strip()
ascii = list(map(chr, range(97,123)))
# [알파벳 하나씩 다 들어옴] = ascii코드 알파벳 범위인 97~123을 사용해서 넣음
# print(ascii)
# print(s)

for i in ascii:
    # print(i) #알파벳 하나씩 뽑으라고
    print(s.find(i))

# 특정 문자열 검색함수인 find 함수는 문자열에서만 동작하고, 찾는 값이 없으면 자동으로 -1을 반환

# 다시 풀기~