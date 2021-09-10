import heapq
def solution(food_times, k):
    heap = []
    n = len(food_times)
    for i in range(n):
        heapq.heappush(heap,(food_times[i] , i+1))

    # 원판에 있는 음식 중 가장 적은 수의 음식
    small_food = heap[0][0]
    prev_food = 0
    while k -((small_food - prev_food) * len(heap)) >= 0:
        # 네트워크 오류 시간까지 하나의 음식이 없어질때까지 걸리는 시간을 빼준다.
        # small_food - prev_food = 현재 가장 작은 음식의 수 - 이전 가장 작은 음식의 수
        k -= (small_food - prev_food) * len(heap)
        # 업데이트
        prev_food, idx = heapq.heappop(heap)
        if not heap:
            return -1
        small_food = heap[0][0]
    heap.sort(key=lambda data : data[1])

    return heap[k % len(heap)][1]
    # 원판 인덱스가 1부터 시작한다해도, 낮은 수의 음식 요소를 빼주게 되니 재배열된 k % len(heap)의 인덱스로
    # 다시 시작하는 원판의 인덱스가 결정된다.
solution([3,1,2],5)