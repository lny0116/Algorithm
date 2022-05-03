def reorderLogFiles(logs):
    letter=[]
    num =[]

    for i in logs:
        if i.split()[1].isdigit(): #나눈 1번째 문자열이 숫자 형태면 >> dig1 '8' 1 5 1
            num.append(i)
            # print(num)
        else:
            letter.append(i)

    letter.sort(key=lambda x: (x.split()[1:],x.split()[0]))
    # 뒤에 문자열이 몇 개올지 모르니 슬라이싱으로 표현

    return letter+num

# 아직 뭐가 들어갈지 몰라서 split이 자동완성이 안된다
# 문자 구성이 먼저 와야하고
# 문자가 동일할 경우엔 식별자 순으로 해야함

print(reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
print(reorderLogFiles(logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))