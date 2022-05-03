# 75 ms	13.8 MB
# http://melonicedlatte.com/python/2017/02/23/152309.html
# https://steadiness-193.tistory.com/203
# re 라이브러리에 대한 설명 = 문법 == re.sub（'찾을 패턴', '변경할 내용', 원본）

# https://latte-is-horse.tistory.com/200
# 리스트의 특정 원소 모두 제거하기

import re
from collections import Counter

def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    paragraph = re.sub("[!?',;.]", ' ',paragraph) #특무문자들을 제거

    p =[]
    for i in paragraph.lower().split():
        p.append(i) #대소문자랑 공백없이 넣음

    for i in banned:
        # print(i)
        if i in p: 
            p = [j for j in p if j not in i]
            # 제거 문자가 없는 데이터만 새로운 리스트에 저장해 특정 값을 제거하는 방법
            
    # print(p)


    cnt = Counter(p)
    # print(cnt)
    return cnt.most_common(1)[0][0]
    # counter에서 어떻게 뽑아야할지 모르겠어서 마지막 부분은 답지를 참고함. most_common
    
       

print(mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
print(mostCommonWord(paragraph = "a.", banned = []))
print(mostCommonWord(paragraph = "a, a, a, a, b,b,b,c, c", banned = ['a']))
