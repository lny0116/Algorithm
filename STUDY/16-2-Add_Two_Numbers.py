# 79 ms	13.9 MB
# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ''
        s2 = '' #str 변환

        # print(type(s1))
        
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next

        # sum = int(reversed(l1)) + int(reversed(l2))
        sum = int(s1[::-1]) + int(s2[::-1]) #다시 숫자형으로 바꾸고 끝서부터 합산

        if sum != 0:
            sum = str(sum)
        else:
            return ListNode(0)

        res = ListNode(val= sum[-1])
        revnode = res
        for val in sum[-2::-1]: #연결리스트 뒤집기
            revnode.next = ListNode(val)
            revnode = revnode.next

        return res


# https://weejw.tistory.com/503 참고 사이트
# 문자열로 이어 붙이고 숫자로 변환해서 계산해가지고 다시 연결리스트로 바꾼 것