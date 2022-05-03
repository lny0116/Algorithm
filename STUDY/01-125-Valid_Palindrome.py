def isPalindrome(s: str) -> bool:
    text = []

    for i in s:
        if i.isdigit() or i.isalpha():
            text.append(i.lower())
    # print(text)

    is_true = list(reversed(text) )

    if text != is_true:
        return False

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))