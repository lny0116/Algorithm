import sys

input=sys.stdin.readline

n=int(input())

for i in range(1,n+1):
    print(('*'*i).rjust(n))

    # rjust(전체 자리 숫자,공백에 채울 문자) 함수는 오른쪽 정렬로 출력해주는 함수!!
    # 처음에 틀린 이유는 내가 전체 자리 숫자 영역에 5로 박아서.. n input만큼 해주면 되는거라
    # 바로 수정해서 성공!