# https://cotak.tistory.com/137
# isdigit() 메서드를 사용하여 Python에서 주어진 문자가 숫자인지 확인
# isalpha() 주어진 문자열이 알파벳으로만 구성되어 있는지 판별한다. 공백이 있으면 False를 반환

# https://www.delftstack.com/ko/howto/python/case-insensitive-string-comparison-in-python/
# lower()메서드를 사용한 대소문자를 구분하지 않는 문자열 비교

class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = []

        for i in s:
            if i.isdigit() or i.isalpha():
                text.append(i.lower())
        # print(text)

        is_true = list(reversed(text))

        if text != is_true:
            return False

        return True
