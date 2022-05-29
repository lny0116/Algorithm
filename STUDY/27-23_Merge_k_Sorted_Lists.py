# 213 ms 17.8 MB
# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list[ListNode]):
    head = ListNode(None)
    now = head #temp
    h = []

    # 각 연결 리스트의 루트(첫 번째 노드)를 힙에 저장
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(h, (lists[i].val, i)) #1번째 노드 힙에 추가 / i는 i번째 목록
            lists[i] = lists[i].next
    
    # 힙 추출 이후 다음 노드는 다시 저장
    while h: #힙이 비워질 때까지 반복
        val, i = heapq.heappop(h) #1번째 노드를 팝
        now.next = ListNode(val) #temp 목록의 다음 노드로
        now = now.next

        if lists[i]:
            heapq.heappush(h, (lists[i].val, i)) #1번째 노드 추가
            lists[i] = lists[i].next
    
    return head.next

# import heapq

# def mergeKLists(lists: list):
#     h = []
    
#     for j in range(len(lists)):
#         for i in lists[j]:
#             heapq.heappush(h,i)

#     return sorted(h)

print(mergeKLists([[1,4,5],[1,3,4],[2,6]]))
print(mergeKLists([]))
print(mergeKLists([[]]))

# 책과 의견 참고