# 126 ms	17.8 MB
# https://leetcode.com/problems/group-anagrams/


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anag = {}
    for i in strs:
        # print(i)
        # b = sorted(i)
        # print(b)
        a = ''.join(sorted(i)) # 쪼개서 정렬한 거 다시 공백없이 붙이고
        # print(a)
        # print(anag)
        anag[a] = anag.get(a,[]) + [i] # 키 값 추가를 리스트에 담고 그 리스트에 i를 추가
    # print(anag)
    return anag.values() #값만 추출




print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(strs = [""]))
print(groupAnagrams(strs = ["a"]))

# 일단 딕셔너리+정렬 사용해야한다는거 책 통해서 알았음ㅎ 펼치자마자 보이더라 ㅎㅎ
# sorted(): key=옵션을 지정해 정렬을 위한 키, 함수를 별도로 지정 가능하다.
# https://slowstarter0404.tistory.com/79
# 딕셔너리.get(접근할 키) = 키 값 추가하는 것