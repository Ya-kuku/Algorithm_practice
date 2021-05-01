import heapq
import sys

# 중앙값 기준으로 작은 값 = left, 큰 값 = right
left, right = [], []
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        # max_heap.
        heapq.heappush(left, (-num, num))
    else:
        # min_heap.
        heapq.heappush(right, (num, num))

    # 왼쪽은 최대힙, 오른쪽은 최소힙
    # 오른쪽 값에 원소가 있으면서,
    # 왼쪽 값이 오른쪽 값보다 큰 경우 조건에 위배
    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right, (left_value, left_value))
        heapq.heappush(left, (-right_value, right_value))

    print(left[0][1])