class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if self.square(num):
            return True
        
    # 완전제곱수 판별 함수
    def square(self, n):
        # e = int(n**0.5)**2 == n
        # print(e)
        return int(n**0.5)**2 == n
