#더블 링크드리스트

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        # 맨뒤에서도 검색이 가능해서, 최초의 데이터는 앞이랑 뒤가 정보가 같게됨
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            #셀프헤드를 특정 변수에 담아두기
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

double_linked_list = NodeMgmt(0)
for data in range(1,10):
    double_linked_list.insert(data)
double_linked_list.desc()

