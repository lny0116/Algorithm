# 70 ms	14 MB
# https://leetcode.com/problems/remove-duplicate-letters/

from collections import Counter

def removeDuplicateLetters(s: str) -> str:
    cnt = Counter(s)
    seen = set()
    stack = []

    for i in s:
        cnt[i] -= 1
        if i in seen:
            continue

        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and i < stack[-1] and cnt[stack[-1]] > 0:
            seen.remove(stack.pop())

        stack.append(i)
        seen.add(i)

    return ''.join(stack)


print(removeDuplicateLetters("bcabc"))
print(removeDuplicateLetters("cbacdcbc"))

# 책 참고
# https://www.daleseo.com/python-collections-counter/ → counter class 사용 방법
