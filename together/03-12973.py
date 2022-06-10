# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = 1
    res = []

    for i in s:
        if len(res) == 0:
            res.append(i) # 마지막에 들어감
        else:
            if i == res[-1]:
                res.pop()
            else:
                res.append(i)

    if len(res) == 0:
        return answer
    else:
        return 0


print(solution('baabaa'))
print(solution("cdcd"))