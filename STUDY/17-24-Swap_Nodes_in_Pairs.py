# 30 ms	13.9 MB
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head # 1
        
        while head and head.next:
            # b가 head를 가리키도록 할당
            b = head.next #2
            head.next = b.next #3
            b.next = head # 1로 가게

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
            # 3, 4가 4, 3으로 바꼈을 때 1, 2 쪽의 2를 4와 연결시키기 위해서는
            # prev가 꼭 필요하고 매 반복마다 바꿔주어야 한다.

        return root.next

# https://ihp001.tistory.com/75 설명 참고 블로그 [베이스는 책]