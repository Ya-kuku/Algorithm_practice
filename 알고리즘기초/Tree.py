class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self,head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            # 왼쪽으로 가야한다
            if value < self.current_node.value:
                # 만약에 왼쪽으로 갔을 경우 해당 브랜치에 값이 있다면
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    # 만약에 없다면 값을 넣어주기
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    # 이진 탐색 코드
    def search(self, value):
        self.current_node = self.head
        # 순회를 시작하니까 값이 있을경우만 while문 실행
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                # 여기서 없으면 None으로 되기때문에 while문 돌아갔을 때 실행 중지됨
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self,value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            return False

        # 이후부터 case들을 분리해서, 코드 작성

        #self.current_node 가 삭제할 Node, self.parent는 삭제할 Node의 parent Node인 상태

        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node

        # 삭제할 노드가 자식을 한개 가지고 있는경우
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left

        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # 삭제할 노드가 자식노드를 두 개 가지고 있을 경우
        if self.current_node.left != None and self.current_node.right != None:
            # case 3-1
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.current_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    # 가장 작은값을 찾았으니 그 가장작은 노드의 부모 노드의 왼쪽 브랜치를 끊어줘야함
                    self.change_node_parent.left = None
                # 삭제할 노드의 부모 노드에다가 연결
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left

        # case 2
        else:
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None
            self.parent.right = self.change_node
            self.change_node.left = self.current_node.left
            self.change_node.right = self.current_node.right
head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

print(BST.search(7))




