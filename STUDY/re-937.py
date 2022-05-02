# 63 ms	14.1 MB

def reorderLogFiles(logs):
    # num = []
    # for i in range(1,10):
    #     num.append(str(i))
    # print(num)

    letter = []
    digit = []

    # for i in logs:
    #     # if i.split()[1] == (ord(i) >= 48 and ord(i) <= 57):
    #     for j in num:
    #         if i.split()[1] == j:
    #             digit.append(i)
    #             print(digit)
    #         else:
    #             letter.append(i)
    #             print(letter)

    # letter.sort(key=lambda x: (x.split()[1:],x.split()[0]))

    # return letter+digit


    for i in logs:
        if i.split()[1].isdigit():
            digit.append(i)
        else:
            letter.append(i)

    # 문자 구성이 먼저 오게 sort
    letter.sort(key=lambda x: (x.split()[1:],x.split()[0]))

    return letter+digit


print(reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
print(reorderLogFiles(logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))