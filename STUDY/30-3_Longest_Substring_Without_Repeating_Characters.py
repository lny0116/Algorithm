# 74 ms	14 MB
# https://leetcode.com/problems/longest-substring-without-repeating-textaracters/

def lengthOfLongestSubstring(s: str) -> int:
    dic, res, start = {}, 0, 0
    for i, text in enumerate(s):
        if text in dic:
            res = max(res, i-start) # 문자 총 길이
            start = max(start, dic[text]+1) # 문자열 인덱스의 시작을 다음 인덱스로 업데이트
        dic[text] = i # dic안에 text가 없으면 해당 i를 넣거나, 해당 i 업데이트
    return max(res, len(s)-start)

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))