# 37 ms	14 MB
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # @staticmethod
    def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
        result = ListNode()
        current = result

        while list1 and list2: # 둘 다 존재할 때
            if list1.val < list2.val:
                current.next = list1 #현재의 노드 다음을 list1로
                list1 = list1.next #list1은 list1의 다음으로 (연결)
            else:
                current.next = list2
                list2 = list2.next

            current = current.next # 현재에서 위의 반복문을 통해 연결하고

        current.next = list1 or list2 # 그렇게 완성된 현재의 다음을 또 연결

        return result.next #첫 시작부터 다음 순으로 출력


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
print(Solution.mergeTwoLists(l1, l2))