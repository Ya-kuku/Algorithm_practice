import heapq
import sys
def solution(scoville, K):
    if K == 0:
        return 0
    if sum(scoville) == 0 or len(scoville) == 1:
        print(-1)
        sys.exit()

    heap = []
    for i in scoville:
        heapq.heappush(heap,i)
    cnt = 0
    while 1:
        if heap[0] >= K:
            return cnt
        else:
            if len(heap) > 1:
                a = heapq.heappop(heap)
                b = heapq.heappop(heap)
                tmp_scovile = a + (b*2)
                heapq.heappush(heap,tmp_scovile)
                cnt += 1
            else:
                return -1

    return cnt

a = [1,2,3,9,10,12]
print(solution(a,7))