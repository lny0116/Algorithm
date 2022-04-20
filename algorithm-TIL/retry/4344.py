import sys

input = sys.stdin.readline

c = int(input())

for i in range(c):
    score = list(map(int,input().split()))
    avr = sum(score[1:])/score[0]
    
    cnt=0
    for i in score[1:]: #일단 여기서 0인덱스 제외하고 뽑아야 반례가 안 나오고
        if i>avr:
            cnt+=1
    total = cnt/score[0]*100 #얘는 반복할 필요가 없잖아? 빼줘 포문 밖으로
    #지금 평균이상인 애들 카운트 끝나면 돌 앤데, 안에서 카운트 0인데
    # 같이 반복할 이유가 없음 total은.. 그래서 빼주는겁니다~
    print(f'{total:.3f}%')

# 한 번만 다시 풀자 ㅎㅎ