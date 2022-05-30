# 574 ms	17.5 MB
# https://leetcode.com/problems/design-hashmap/

from collections import defaultdict

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000 #적당히 설정
        self.table = defaultdict(ListNode) #각 listnode에 담을 기본 자료형 중
        # 편리하게 구현하기 위해 존재하지 않는 키를 생성해주는 defaultdict 사용

    def put(self, key: int, value: int) -> None:
        idx = key % self.size #size 개수만큼 모듈로 연산을 한 나머지를 해시값으로 정하는 방식

        #해당 인덱스에 없으면 키, 값을 삽입하고 바로 종료
        if self.table[idx].value is None:
            self.table[idx] = ListNode(key, value)
            return
        # value 유무로 따진 이유: defaultdict가 존재하지 않는 인덱스로 조회를 시도할 때
        # 에러를 발생하지 않고, 바로 디폴트 객체를 생성해서

        # 해당 인덱스에 노드가 존재하는 경우 (해시 충돌이 발생한 경우 / 개별 체이닝 방식으로 해결)
        p = self.table[idx]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key,value) #에러없이 정상 진행이면 p.next에 새 노드 생성+연결
        # 기존에 존재하지 않았던 키면 맨 마지막에 새로운 노드 연결

    def get(self, key: int) -> int:
        idx = key % self.size
        if self.table[idx].value is None:
            return -1

        p = self.table[idx]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
        # 해싱 결과에 하나 이상의 노드가 존재한다는 얘기
        # p.next로 탐색하며 일치 키 찾는데, 찾으면 값을, 못 찾으면 루프를 빠지면서 -1리턴

    def remove(self, key: int) -> None:
        idx = key % self.size
        if self.table[idx].value is None:
            return
        p = self.table[idx]
        if p.key == key:
            self.table[idx] = ListNode() if p.next is None else p.next
            return
        # 첫 번째 노드일 때 p.next is None이라면 유일한 노드를 삭제하는 것이므로 모두 없애야 함
        # 여기서는 defaultdict를 이용해서 매번 빈 노드를 생성해서 ㄱㅊ
        
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
        # 연결 리스트인 노드를 삭제하면 prev는 이전, p는 현재 노드로 계속 탐색하다 일치 노드 찾으면
        # 이전과 현재 노드의 다음으로 연결. 즉, 현재 노드를 아무런 연결 고리가 없도록 끊음
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# 책 참고... 뭔 말인지 이해 부족함... -_-