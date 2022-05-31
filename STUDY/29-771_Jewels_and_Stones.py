# 69 ms	14 MB
# https://leetcode.com/problems/jewels-and-stones/

from collections import defaultdict

def numJewelsInStones(jewels: str, stones: str) -> int:
    how = defaultdict(int)
    cnt = 0

    for i in stones:
        how[i] +=1 # 돌 단어 하나씩 카운트

    for i in jewels:
        cnt += how[i] # how[i]의 단어와 일치할 때 cnt 업
    
    return cnt


print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(numJewelsInStones(jewels = "z", stones = "ZZ"))
