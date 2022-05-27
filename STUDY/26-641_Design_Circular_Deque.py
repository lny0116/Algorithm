# 137 ms 14.7 MB
# https://leetcode.com/problems/design-circular-deque/

from collections import deque

class MyCircularDeque:

    # Initializes the deque with a maximum size of k.
    def __init__(self, k: int):
        self.q = deque()
        self.maxSize = k       

    # Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
    def insertFront(self, value: int) -> bool:
        if len(self.q) < self.maxSize:
            self.q.insert(0,value) #add value front
            return True
        else:
            return False
        
    # Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
    def insertLast(self, value: int) -> bool:
        if len(self.q) < self.maxSize:
            self.q.append(value)
            return True
        else:
            return False
        
    # Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
    def deleteFront(self) -> bool:
        if self.q:
            self.q.popleft() #front
            return True
        else:
            return False
        
    # Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
    def deleteLast(self) -> bool:
        if self.q:
            self.q.pop() #back
            return True
        else:
            return False
        
    # Returns the front item from the Deque. Returns -1 if the deque is empty.
    def getFront(self) -> int:
        if self.q:
            return self.q[0]
        else:
            return -1
        
    # Returns the last item from Deque. Returns -1 if the deque is empty.
    def getRear(self) -> int:
        if self.q:
            return self.q[-1]
        else:
            return -1
        
    # Returns true if the deque is empty, or false otherwise.
    def isEmpty(self) -> bool:
        return len(self.q) == 0
        
    # Returns true if the deque is full, or false otherwise.
    def isFull(self) -> bool:
        return len(self.q) == self.maxSize
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

# https://www.daleseo.com/python-queue/ [insert 넣는 거]
# https://wikidocs.net/104977 [문법]