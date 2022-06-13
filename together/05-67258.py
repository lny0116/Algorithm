# https://programmers.co.kr/learn/courses/30/lessons/67258
# 투포인터로 푸는거였답니다..! 짜잔..!ㅠㅠ

def solution(gems):
    answer = []
    gems_len = len(gems)+1 # gems의 길이 (+1 해줘야 다 포함됨)

    start, end = 0, 0 # 시작, 끝점 체크

    check_gems_len = len(set(gems)) # 중복 제외한 보석의 종류
    contained = {} # 현재 구간에 포함된 보석들(종류: 갯수)

    while end < len(gems): # 구간의 끝 점이 gems의 길이보다 작을 동안
        if gems[end] not in contained: # 현재 끝 점의 보석이 contained에 없다면(이 종류가 처음 발견되었다면)
            contained[gems[end]] = 1 # dictionary에 개수 추가
        else:
            contained[gems[end]] += 1 # 이미 있으면 dictionary에 +1
            
        end += 1 # 끝 점 증가

        if len(contained) == check_gems_len: # 현재 구간 내 보석의 종류의 갯수가 전체 종류의 갯수와 같다면 (현재 구간 내 모든 종류가 있다면)
            while start < end: # start 가 end 보다 같을 때까지 증가
                if contained[gems[start]] > 1: # start에 해당하는 보석이 구간 내에 하나 이상 있다면
                    contained[gems[start]] -= 1 # 구간 내 보석 하나 감소(start 의 보석 뺄거니까)
                    start += 1 # start 증가
                elif gems_len > end - start: # 기존의 구간 최단거리보다 현재의 구간거리가 더 짧다면
                    gems_len = end - start
                    answer = [start+1, end] # answer와 최단거리 갱신
                    break
                else:
                    break

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))