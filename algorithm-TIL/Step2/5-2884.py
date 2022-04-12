# 입력 시간은 24시간 표현을 사용
# 하루의 시작은 0:0(자정)이고,
# 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용

import sys

input=sys.stdin.readline

h,m=map(int, input().split()) #시간,분

if m>=45: #크면 -45분해도 타격 x
    print(h,m-45)
elif h>0 and m<45: #0시 보단 커야지 m이 45분보다 작아도 h-1(60분)할 수 있고, m+15(60-45)할 수 있음
    print(h-1,m+15)
else: #위 조건이 다 아니면, h<=0 이렇게 시작되는데, 이러면 0시에서 빼면 23시니까 바로 23시 출력
    print(23,m+15)


# 내가 푼 식인데, 아닌 거같아서 참고하러 감^^... 다시풀어라~ 별표에 담음
# if h<=23:
#     if m<=59:
#         mTotal= (m+60)-45
# else:
#     hTotal=(h-1)

# print(hTotal,mTotal)