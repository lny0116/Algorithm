# 29 ms	13.8 MB
# https://leetcode.com/problems/valid-parentheses/7

def isValid(s: str) -> bool:
    li = []
    dic = {')':'(','}':'{',']':'['} #거꾸로 해야 내가 짠 코드에 들어맞아

    for i in s: #i = 0번째 인덱스 == '('임 / 그리고 다음은 ')'
        if i not in dic: #dic 키값과 일치가 x / )는 dic의 키값과 일치해 그래서 elif으로 감
            li.append(i) #i값 넣어줘
        elif not li or dic[i] != li.pop():
            return False

    return len(li) == 0

# print(isValid("()[]{}"))

# 책 참고
