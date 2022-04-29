import sys

input=sys.stdin.readline

n = set(range(1,10001))
remove_set = set() #생성자가 있는 숫자 set

for i in n: # i = 850
    for j in str(i): #j = '8', '5', '0'
        i+=int(j) # i = 850+8+5+0
    remove_set.add(i) #집합에 요소를 추가할 때 , add()

self_num = sorted(n - remove_set) #set의 - 연산자로 차집합을 구하고 정렬
for i in self_num: 
    print(i)