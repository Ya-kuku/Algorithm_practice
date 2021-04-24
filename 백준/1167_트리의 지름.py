# 다익스트라 풀이
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n = int(input())
s = [[] for i in range(n + 1)]
def dijkstra(start):
    d = [100000000 for i in range(n + 1)]
    d[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        we, ne = heappop(heap)
        for n_n, n_w in s[ne]:
            wei = n_w + we
            if wei < d[n_n]:
                d[n_n] = wei
                heappush(heap, [wei, n_n])
    return d
for _ in range(1, n+1):
    tmp = list(map(int,input().split()))
    cur_node = tmp[0]
    for i in range(1,len(tmp)-1,2):
        s[cur_node].append([tmp[i], tmp[i+1]])
        s[tmp[i]].append([cur_node, tmp[i+1]])
d_ = dijkstra(1)
print(max(dijkstra(d_.index(max(d_[1:])))[1:]))