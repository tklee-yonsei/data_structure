from data_structure.ds.interface.data_structure import DataStructure


class Node:
    """연결 리스트의 노드 클래스"""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListpinesound(DataStructure):
    """LinkedListpinesound 클래스."""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def add(self, value):
        """새로운 노드를 리스트의 맨 앞에 추가합니다."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def remove(self, value):
        """주어진 값을 가진 노드를 제거합니다."""
        if not self.head:
            return False
        
        # 헤드 노드가 삭제할 값을 가지고 있는 경우
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return True
        
        # 그 외의 노드들을 확인
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
            
        return False

    def search(self, value):
        """주어진 값을 가진 노드를 찾습니다."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False