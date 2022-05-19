# 	49 ms	14 MB
# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        root = start = ListNode(None)
        root.next = head

        # start와 end set
        for i in range(left-1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for i in range(right-left):
            temp = start.next #temp는 start의 다음에 고정
            start.next = end.next
            end.next = end.next.next
            start.next.next = temp

        return root.next

# 책 참고


        # root = start = ListNode(None)
        # end = start.next
        # while start:
        #     if start.next == left:
        #         start.next = right
        #         right.next = left.next
        #         left.next = end

        # return start