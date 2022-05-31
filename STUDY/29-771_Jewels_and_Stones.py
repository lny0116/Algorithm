# 69 ms	14 MB
# https://leetcode.com/problems/jewels-and-stones/

from collections import defaultdict

def numJewelsInStones(jewels: str, stones: str) -> int:
    how = defaultdict(int)
    cnt = 0

    for i in stones:
        how[i] +=1

    for i in jewels:
        cnt += how[i]
    
    return cnt


print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(numJewelsInStones(jewels = "z", stones = "ZZ"))