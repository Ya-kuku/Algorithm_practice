import heapq

N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int,input().split())))
arr.sort()

heap = []
for i in arr:
    # 데드라인의 수
    a = i[0]
    heapq.heappush(heap,i[1])
    # 데드라인의 문제를 초과했을경우 가장 작은 원소 값 삭제
    if a < len(heap):
        heapq.heappop(heap)

print(sum(heap))


