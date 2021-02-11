# 부모 노드 인덱스 번호 = 자식 노드 인덱스 번호 //2
# 왼쪽 자식 노드 인덱스 = 부모 노드 인덱스 * 2
# 오른쪽 자식 노드 인덱스 = 부모 노드 인덱스 * 2 + 1
# heap은 완전 이진 트리이기 때문에 배열 사용

# 최대 힙
class Heap:
    def __init__(self,data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    # 노드가 이동해야 하는지 판단하는 함수
    def move_up(self, inserted_idx):
        # 루트 노드이면 움직일 필요 x
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2
        # 부모 노드보다 큰 경우 True 반환, 아닐시 False 반환
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self,data):
        # 데이터 추가 부분
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)

        # 끝까지 들어간 노드 숫자의 인덱스를 알기 위해서(마지막)
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx //2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        return True

    # 데이터를 내려야 하는지 확인하는 함수
    def move_down(self,popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        # case 1 : 왼쪽 자식 노드도 없을 때
        # 전체 길이보다 크거나 같은 경우로 비교
        if left_child_popped_idx >= len(self.heap_array):
            return False

        # case 2 : 오른쪽 자식 노드만 없을 때
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False

        # case 3 : 왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            # 왼쪽이 큰 경우에
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            # 오른쪽이 큰 경우에
            else:
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

    def pop(self):
        # 일종의 방어 코드
        if len(self.heap_array) <= 1:
            return None

        # 첫 idx의 데이터가 None이라서 1번으로
        returned_data = self.heap_array[1]
        # 마지막 데이터를 제일 위로 올림
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        # 추출된 데이터는 루트에 있어서 idx 1부터 시작
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # case 2 : 오른쪽 자식 노드만 없을 때
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
                    return True

            # case 3 : 왼쪽, 오른쪽 자식 노드 모두 있을 때
            else:
                # 왼쪽이 큰 경우에
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[popped_idx] , self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_popped_idx
                # 오른쪽이 큰 경우에
                else:
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = right_child_popped_idx
        return returned_data

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)

print(heap.pop())
print(heap.heap_array)