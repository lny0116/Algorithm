# 145 ms 14.2 MB
# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = list()
        
        for i in nums:
            heapq.heappush(heap, -i)
            
        for i in range(1, k):
            heapq.heappop(heap)
            
        
        return -heapq.heappop(heap)
