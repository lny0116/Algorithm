# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    stack = ['zero','one','two','three','four','five','six','seven','eight','nine']
    res = ''

    for idx, num in enumerate(stack): # idx와 num이 같으니까 매핑
        # print(idx, num)
        if num in s:
            s = s.replace(num, str(idx)) # 인덱스 번호로 교체
            # print(s)
        res = s

    return int(res)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))