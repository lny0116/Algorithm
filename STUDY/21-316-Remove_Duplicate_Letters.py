# 70 ms	14 MB
# https://leetcode.com/problems/remove-duplicate-letters/

from collections import Counter

def removeDuplicateLetters(s: str) -> str:
    cnt = Counter(s)
    # print(cnt) # 1번째= Counter({'b': 2, 'c': 2, 'a': 1})
    seen = set()
    # print(seen) #set() 출력
    stack = []

    for i in s:
        cnt[i] -= 1 #카운터 목록에서 하나 제거하고
        if i in seen:
            continue

        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and i < stack[-1] and cnt[stack[-1]] > 0:
            #stack에 있는 문자가 더 크고 cnt가 0보다 크면
            seen.remove(stack.pop()) #seen과 stack에서 없앰

        #그리고 i를 다시 넣어줌
        stack.append(i)
        seen.add(i)

    return ''.join(stack)


print(removeDuplicateLetters("bcabc"))
print(removeDuplicateLetters("cbacdcbc"))

# 책 참고
# https://www.daleseo.com/python-collections-counter/ → counter class 사용 방법
