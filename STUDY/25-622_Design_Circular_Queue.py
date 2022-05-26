# 62 ms	14.6 MB
# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.size = k
    
    # Inserts an element into the circular queue. Return true if the operation is successful.
    def enQueue(self, value: int) -> bool:
        if len(self.q) < self.size:
            self.q.append(value)
            return True
        else:
            return False
    
    # Deletes an element from the circular queue. Return true if the operation is successful.
    def deQueue(self) -> bool:
        if len(self.q) == 0:
            return False
        
        del self.q[0]
        return True

    # Gets the front item from the queue. If the queue is empty, return -1.
    def Front(self) -> int:
        return -1 if len(self.q) == 0 else self.q[0]

    # Gets the last item from the queue. If the queue is empty, return -1.
    def Rear(self) -> int:
        return -1 if len(self.q) == 0 else self.q[-1]

    # Checks whether the circular queue is empty or not.
    def isEmpty(self) -> bool:
        return True if len(self.q) == 0 else False

    # Checks whether the circular queue is full or not.
    def isFull(self) -> bool:
        return True if len(self.q) == self.size else False        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# https://ooyoung.tistory.com/49 [del 사용법 = 인덱스로 삭제] // 선입선출이라 0인덱스 del
# 책 및 의견 참고