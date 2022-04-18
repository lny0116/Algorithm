import sys

input=sys.stdin.readline

li = []
for i in range(3):
    n=int(input())
    li.append(n)

mul = list(str(li[0]*li[1]*li[2]))
#['1', '7', '0', '3', '7', '3', '0', '0']

for i in range(10):
    print(mul.count(str(i)))
    #이걸 내가 자꾸 리스트 요소 int 안 된다고 써있어서 str로 바꿨으면서
    # 찾는 것도 str로 바꿔줘야하는데, 안 바꿔줘서 실패했던 거였음..ㅎ
    # str(i)를 했어야한다~ 안 보고 풀긴 함... 구글링 제외