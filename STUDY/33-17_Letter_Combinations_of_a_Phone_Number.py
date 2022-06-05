# 28 ms	13.9 MB
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


def letterCombinations(digits: str) -> list[str]:
    dic = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    res = []

    if len(digits) == 0:
        return res
    
    dfs(dic, digits, '', res)
    return res

def dfs(dic, digits, path, res):
    if not digits:
        res.append(path)
        return 
    for c in dic[digits[0]]:
        dfs(dic, digits[1:], path+c, res)


print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))