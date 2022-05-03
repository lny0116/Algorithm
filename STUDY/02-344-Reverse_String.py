def reverseString(s) -> None:
    # 처음 생각했던 코드 - return을 써서 안됨..
    # s = s[::-1]
    # return s
    s[0:] = s[::-1]
    


print(reverseString(["h","e","l","l","o"]))
print(reverseString(["H","a","n","n","a","h"]))


# 문자열을 뒤집는다 == 슬라이싱으로 뒤집으면 되겠지 생각
# 근데 return값을 사용하면 안된다고 해서, 그럼 처음부터 있던 애를 뒤집은 애로 덮어씌우자고 생각