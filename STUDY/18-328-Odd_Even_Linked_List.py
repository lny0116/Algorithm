# 81 ms	16.6 MB
# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head is None:
            return None #예외처리를 해주지 않으면 런타임에러가 뜸
        
        odd = head
        even = head.next
        even_head = head.next #짝수 시작은 even과 같음

        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next = odd.next.next #2번 이동하게 설정
            odd = odd.next #odd의 위치 이동
            even.next = even.next.next
            even = even.next

        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head

        return head #머리부터 쭉 출력

# 책 참고
