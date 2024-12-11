from data_structure.ds.interface.data_structure import DataStructure


class Node:
    """Node 클래스는 Linked List의 단일 노드를 표현합니다."""
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_List_mimsa(DataStructure):
    """LinkedList 클래스."""
    
    def __init__(self):
        self.head = None

    def add(self, value):
        """리스트의 끝에 값을 추가합니다."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, value):
        """리스트에서 특정 값을 제거합니다."""
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:  # 중간 또는 끝의 노드 삭제
                    prev.next = current.next
                else:  # 첫 번째 노드 삭제
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False  # 값이 없을 경우


    def search(self, value):
        """리스트에서 특정 값을 검색합니다."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False