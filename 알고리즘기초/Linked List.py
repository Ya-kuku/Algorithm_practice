# # 노드가 만들어질 때마다 생성
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# # 인자를 넣어줄때 다음 데이터와 주소값까지 넣어주는 방식 없으면 None으로 생성
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
#
# #노드와 노드 연결하기(포인터 활용)
# node1 = Node(1)
# node2 = Node(2)
#
# #노드1의 다음주소가 노드2
# node1.next = node2
#
# #가장 앞에 있는 주소를 지정
# head = node1
#
#
# #링크드 리스트로 데이터 추가하기
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
#
# def add(data):
#     node = head
#     # 마지막 노드를 찾기 위한 코드
#     while node.next:
#         node = node.next
#     node.next = Node(data)
#
#     node1 = Node(1)
#     head = node1
#     for index in range(2, 10):
#         add(index)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    # 노드 추가 뒤에
    def add(self, data):
        # 일종의 방어코드, 만약에 head 값이 없으면 맨 앞에 있는 노드를 만든다
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    # 전체 노드 출력, 링크드 리스트를 순회
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        # 이것도 일종의 방어코드
        if self.head == '':
            print('해당 값을 가진 노드가 없습니다')
            return

        # 헤드를 삭제
        if self.head.data == data:
            temp = self.head
            # 현재 가지고 있는 head의 주소를 다음 노드의 주소로 바꿔주는 작업
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    # 현재 노드에서 다음 삭제할 노드의 주소 정보를 가리킴
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next


linkedlist2 = NodeMgmt(5)
# linkedlist2.desc()
# linkedlist2 = NodeMgmt(5)
for data in range(1,10):
    linkedlist2.add(data)

linkedlist2.desc()

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

print(linkedlist1.head)

linkedlist1.delete(0)
print(linkedlist1.head)

for data in range(1,10):
    linkedlist1.add(data)
# linkedlist1.desc()

linkedlist1.delete(4)
linkedlist1.delete(8)
linkedlist1.desc()
