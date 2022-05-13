# 1073 ms	31.2 MB
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None #역순 연결 리스트 값
        slow = fast = head # 느린,빠른 러너 초기값은 머리부터

        #러너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next #빠른 러너는 이동 두칸씩이라서 두 번 적어줌
            rev, rev.next, slow = slow, rev, slow.next #느린 러너는 한 칸씩
            #첫 rev>none인데 러너 이동하면서 1>none 2>1>none으로 점점 이전값으로 연결구조
        if fast: # 홀수일 때 (짝수일 땐 상관x)
            slow = slow.next #느린 러너 한 칸 움직이게 해서 중앙값을 빗기게
            # = 여기서 3이 중앙값이라 펠린드롬 체크에서 배제되어야 하기에 == (fast != none)

        # 펠린드롬 여부 확인 / 역순으로 만든 연결 리스트를 반복
        while rev and rev.val == slow.val: # slow의 나머지 이동 경로와 역순으로 만든 rev노드 비교
            slow, rev = slow.next, rev.next
            # 정상적으로 종료되면 slow & rev == none
        
        return not rev # 또는 not slow


print(isPalindrome([1,2,2,1]))
print(isPalindrome([1,2]))

# 책보고 풀었습니다..!