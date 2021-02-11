import heapq
N = int(input())
array = []
result = []

for _ in range(N):
    data = int(input())
    if data == 0:
        if array:
            result.append(heapq.heappop(array))
        else:
            result.append(0)
    else:
        heapq.heappush(array,data)

for data in result:
    print(data)

