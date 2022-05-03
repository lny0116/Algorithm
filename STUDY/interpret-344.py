def reverseString(s) -> None:
    for i in range(len(s)//2): #s의 길이를 반으로 쪼개
        j = len(s) -1 -i #반복이 돌 때마다 (s의 길이 -1 -i)를 해주고 [바꿀 자리]
        s[i], s[j] = s[j], s[i] #해당 인덱스들의 위치를 말그대로 바꿔줘 ij 에서 ji로 == 리버스
    print(s)

reverseString(["h","e","l","l","o"])
reverseString(["H","a","n","n","a","h"])

#보경언니 승우 코드 짠 거