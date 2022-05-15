# 35 ms	15.3 MB
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None #prev는 이전 결과값(초기값 none)을 가리킴
        
        while head:
            temp = head #head 노드를 temp에 참조하고
            head = head.next #head 움직임
            temp.next = prev #temp.next에 prev를 연결 == temp는 현재 반복 결과물(역순의 첫 노드)
            prev = temp # 반복 첫 과정에 prev가 이전 모든 결과를 담고있어야 해서 temp를 할당
            
        return prev

# https://velog.io/@kynel/파이썬-알고리즘-역순-연결-리스트 참고