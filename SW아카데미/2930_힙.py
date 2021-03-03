import heapq
for tc in range(int(input())):
    N = int(input())
    heap = []
    result = []

    for _ in range(N):
        data = list(input().split())
        if len(data) == 1:
            if heap:
                result.append(heapq.heappop(heap))
            else:
                result.append((-1,-1))
        else:
            heapq.heappush(heap,(-int(data[1]),int(data[1])))

    print('#{}'.format(tc+1,),end=' ')
    for i in result:
        print(i[1],end=' ')
    print()


