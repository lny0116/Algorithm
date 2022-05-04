# 브루트포스로 문제 풀었는데, 시간이 난리남ㅋㅋㅋㅋㅋㅋㅋㅋ
# 9138 ms	13.9 MB
# https://leetcode.com/problems/longest-palindromic-substring/

def longestPalindrome(s: str) -> str:
    l = len(s)

    for i in range(l):
        for j in range(i+1):
            temp = s[j:(l-i+j)] # 계속 줄여가면서 담아
            if temp == temp[::-1]: #앞뒤 같은지 확인 // reversed 안돼
                return temp

print(longestPalindrome(s = "babad"))
print(longestPalindrome(s = "cbbd"))

# https://daebaq27.tistory.com/26
# 브루트포스 설명
# 가능한 모든 부분 문자열을 선택하고, 선택한 부분이 팰린드롬인지 확인