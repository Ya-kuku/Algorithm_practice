import sys
sys.setrecursionlimit(100000)
def dfs(start, tree, weight, ck): # ck로 루트1번에서 시작한 건지, 최장길이 노드를 루트로 한건지 판단
    if ck == 1:
        weight[1] = 0 # 루트 1번 노드 가중치 0으로 설정

    for node, w in tree[start]:
        if(weight[node] == 0):
            weight[node] = weight[start] + w # 현재 가중치 + 다음 노드와 가중치
            dfs(node, tree, weight, ck)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)] # 입력 값 tree 생성
for _ in range(n-1):
    p_node, c_node, w = map(int, sys.stdin.readline().split())
    tree[p_node].append((c_node, w))
    tree[c_node].append((p_node, w))

weight1 = [0 for _ in range(n+1)] # 루트1로부터 길이를 저장
dfs(1, tree, weight1, 1) # 루트 1 시작점으로 해 가장 먼 노드를 찾음
print(weight1)
# 찾은 가장 먼 노드를 시작 노드로 탐색
# 최장경로 노드에서 다시 DFS를 통해 트리지름구하기
start_node = weight1.index(max(weight1[1:]))
weight2 = [0 for _ in range(n+1)]
dfs(start_node, tree, weight2, 2)
print(weight2)
print(max(weight2[1:]))

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
for i in range(1, n):
    p, c, w = map(int, input().split())
    s[p].append([c, w])
    s[c].append([p, w])
d_ = dijkstra(1)
print(max(dijkstra(d_.index(max(d_[1:])))[1:]))


from collections import deque

n=int(input())
tree={i:[] for i in range(n+1)}
for i in range(n-1):
  a,b,weight=map(int, input().split())
  tree[a].append((b,weight))
  tree[b].append((a,weight))

def bfs(s):
  queue=deque()
  queue.append((s,0))
  visited=[0]*n
  visited[s-1]=1

  result=[0,0]
  while queue:
    now,cnt=queue.popleft()
    for i in tree[now]:
      next_number,value=i[0],i[1]
      if visited[next_number-1]==0:
        visited[next_number-1]=1
        queue.append((next_number,cnt+value))
        if result[1]<cnt+value:
          result[0]=next_number
          result[1]=cnt+value

  return result

a=bfs(1)
b=bfs(a[0])
print(b[1])