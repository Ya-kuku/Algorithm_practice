## 일반적인 큐
# import queue
#
# data_queue = queue.Queue()
#
# data_queue.put("funcoding")
# data_queue.put(1)
#
# print(data_queue.qsize())
#
# print(data_queue.get())
# print(data_queue.get())

## LIFO 큐(stack 같은 큐)

# import queue
# data_queue = queue.LifoQueue()
# data_queue.put("첫번째")
# data_queue.put("두번째")
#
# print(data_queue.qsize())
#
# print(data_queue.get())
# print(data_queue.get())

# 2
# 두번째
# 첫번째


## Priority 큐
# import queue
# data_queue = queue.PriorityQueue()
# data_queue.put((10,"korea"))  # 첫번째 숫자가 우선순위고 두번째인자가 데이터 튜플 형식으로 들어감
# data_queue.put((5,"china"))
# data_queue.put((15,"usa"))
#
# print(data_queue.qsize())
#
# print(data_queue.get()) # 우선순위가 5가 제일 높기때문에 china가 먼저 뽑힘
# print(data_queue.get()) # 그 다음 우선순위는 10이기 때문에 korea가 뽑힘


# enqueue, dequeue 구현하기
# queue_list = list()
#
# def enqueue(data):
#     queue_list.append(data)
#
# def dequeue():
#     data = queue_list[0]
#     del queue_list[0]
#     return data

# data_stack = list()
#
# data_stack.append(1)
# data_stack.append(2)
#
# print(data_stack)
# print(data_stack.pop())

stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

for index in range(10):
    push(index)
